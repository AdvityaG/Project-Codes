package message;
import account.Account;
import account.AccountStatus;

import java.util.Date;
import java.util.ArrayList;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;

/**
 * Message creates an Account called from, Date called date, Message called repliedTo, ArrayList of Message called replies and String called body
 * 
 * @author              Advitya Garg
 * @version             1.0
 * @since               1.0
 * @license.agreement   Gnu General Public License 3.0 
 */
public class Message{
    private Account from;
    private Date date;
    private Message repliedTo;
    private ArrayList<Message> replies;
    private String body;

    /**
     * It initialises from, date, repliedTo, replies and body
     *  
     * @param from           It's an Account named from
     * @param repliedTo      It's a Message named repliedTo
     * @param body           It's a String named body
     * @since                1.0
     */

    public Message(Account from, Message repliedTo, String body){
        this.from=from;
        this.repliedTo=repliedTo;
        this.body=body;
        this.date=date;
        if(repliedTo!=null){
            repliedTo.addReply(this);
        }
        replies = new ArrayList<>();
    }

    public Message(BufferedReader br, Message repliedTo) throws IOException{
        this.from=new Account(br.readLine());
        this.date=new Date(Long.parseLong(br.readLine()));
        this.body=br.readLine();
        int num=Integer.parseInt(br.readLine());
        this.replies=new ArrayList<>();
        for(int i=0;i<num;i++){
            String temp=br.readLine();

            Message ms;
            if(temp.equals("message.Post")){
                ms=new Post(from, null, repliedTo,body);
            }
            else{   
                ms=new DirectMessage(from, null, repliedTo, body);
            }
            
            this.replies.add(ms);
        }

        if(this.repliedTo!=null){
            this.repliedTo.addReply(this);
        }
    }

    public void save(BufferedWriter bw) throws IOException{
        bw.write(from + "/n");
        bw.write(""+date+"\n");
        bw.write(""+body+"\n");
        bw.write(""+replies.size()+"\n");
        for(Message m:replies){
            bw.write(m.getClass().getName()); 
            m.save(bw);
        }
    }

    /**
     * returns the Message replied to
     * 
     * @since 1.0
     * @return returns the object repliedTo
     */
    public Message getRepliedTo(){
        return repliedTo;
    }

    /**
     * Getter method to reply null or the value at index
     * 
     * @param index stores the position 
     * @since 1.0
     * @return returns null or the value at index
     */

    public Message getReply(int index){
        if(index>=replies.size() || index<0){
            return null;
        }
        return replies.get(index);
    }

    public int getNumReplies() {
        return replies.size();
    }

    public String getTitle() {
        return "From " + from; // + " on " + date;
    }
    /**
     * the toString method returns date+ from+ repliedTo.from+ all the values in replies+ body
     * 
     * @since 1.0
     * @return returns date+ from+ repliedTo.from+ all the values in replies+ body
     */

    @Override
    public String toString(){
        String prStr="Date: "+date+"\nFrom: "+from+"\n";
        if(repliedTo!=null){
            prStr+="In reply to: "+repliedTo.from+"\n";
        }
        if(replies.size()!=0){
            prStr+="Replies: ";
            for(int i=0;i<replies.size();i++){
                prStr+="["+i+"]"+replies.get(i).from+", " ;
            }
        }
        prStr+=body;
        return prStr;
    }

    /**
     * Adds message to the ArrayList of Message called replies
     * 
     * @param message initialises a Message called message
     * @since 1.0
     */
    private void addReply(Message message){
        replies.add(message);
    }
}