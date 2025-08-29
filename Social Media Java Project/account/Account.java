package account;
import message.Message;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;

/**
 * Account creates a name. ID, nextID and shows status of Account
 * 
 * @author              Advitya Garg
 * @version             1.0
 * @since               1.0
 * @license.agreement   Gnu General Public License 3.0 
 */


public class Account{
    private String name;
    private int id;
    private static int nextID=1;
    AccountStatus status;

    /**
     * It initialises name,ID, nextID and AccountStatus
     * 
     * @param name    It's a name
     * @since         1.0
     * @throws        IllegalArgumentException
     */
    public Account(String name){    
        this.name=name;
        if(name.length()==0){
            throw new IllegalArgumentException();
        }    
        
        id=nextID;
        nextID++;
        status=AccountStatus.Normal;
    }

    public Account(BufferedReader br) throws IOException{
        this.name=br.readLine();
        this.id=Integer.parseInt(br.readLine());
        this.nextID=Integer.parseInt(br.readLine());
        this.status=AccountStatus.valueOf(br.readLine());
    }
    
    public void save(BufferedWriter bw) throws IOException{
        bw.write(name+"\n");
        bw.write(""+id+"\n");
        bw.write(""+nextID+"\n");
        bw.write(""+status+"\n");
    }


    /**
     * It's a setter method to set the status to status
     * 
     * @param status it sets the status to status
     * @since 1.0
     */
    public void setStatus(AccountStatus status){
        this.status=status;
    }

    /**
     * It returns the status if AccountStatus is not Normal
     * 
     * @since 1.0
     * @return returns the status
     */
    public boolean isMuted(){
        return status!=AccountStatus.Normal;
    }

    /**
     * It returns the status if AccountStatus is Blocked
     * 
     * @since 1.0
     * @return returns the status
     */
    public boolean isBlocked(){
        return status==AccountStatus.Blocked;
    }

    /**
     * the toString method returns String name + id or + status 
     * 
     * @since 1.0
     * @return returns the name+id or name+id+[status]
     */
    @Override
    public String toString(){
        String giveId=name+" ("+id+')';
        if(isMuted()){
            giveId+=" ["+status+']';
        }
        return giveId;
    }
}