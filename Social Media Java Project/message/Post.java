package message;
import account.Account;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;

/**
 * Post extends Message class and creates an Account called from, Group called group, Message called repliedTo, and String called body
 * 
 * @author              Advitya Garg
 * @version             1.0
 * @since               1.0
 * @license.agreement   Gnu General Public License 3.0 
 */

public class Post extends Message {
    private Group group;
    /**
     * It initialises from, group, repliedTo and body
     * 
     * @param from           It's an Account named from
     * @param group          It's a Group called group
     * @param repliedTo      It's a Message named repliedTo
     * @param body           It's a String named body
     * @since                1.0
    */
    public Post(Account from, Group group, Message repliedTo,String body){
        super(from,repliedTo,body);
        this.group=group;
    }

    public Post(BufferedReader br,Message repliedTo) throws IOException{
        super(br,repliedTo);
    }

    public void save(BufferedWriter bw) throws IOException{
        bw.write(group+"\n");
    }

    /**
     * the toString method returns group+ toString of its parent class Message
     *  
     * @since 1.0
     * @return returns group+ toString of its parent class Message
     */
    @Override
    public String toString(){
        return group+ super.toString();
    }
}
