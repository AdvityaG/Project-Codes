package message;
import account.Account;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;

/**
 * Post extends Message class and creates an Account called from, Account called to, Message called repliedTo and String called body
 * 
 * @author              Advitya Garg
 * @version             1.0
 * @since               1.0
 * @license.agreement   Gnu General Public License 3.0 
 */

public class DirectMessage extends Message {
    private Account to;
    /**
     * It initialises from, to, repliedTo and body
     * 
     * @param from           It's an Account named from
     * @param to             It's a Account called to
     * @param repliedTo      It's a Message named repliedTo
     * @param body           It's a String named body
     * @since                1.0
    */
    public DirectMessage(Account from, Account to, Message repliedTo,String body){
        super(from,repliedTo,body);
        this.to=to;
    }

    public DirectMessage(BufferedReader br,Message repliedTo) throws IOException{
        super(br,repliedTo);
    }

    public void save(BufferedWriter bw) throws IOException{
        bw.write(to+"\n");
    }

    /**
     * the toString method returns to+ toString of its parent class Message
     *  
     * @since 1.0
     * @return returns to+ toString of its parent class Message
     */
    @Override
    public String toString(){
        return to+ super.toString();
    }
}