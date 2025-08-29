package message;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;

/**
 * Group creates a name and gives a status of active or not active
 * 
 * @author              Advitya Garg
 * @version             1.0
 * @since               1.0
 * @license.agreement   Gnu General Public License 3.0 
 */


public class Group {
    private String name;
    private boolean active;  
    
    /**
     * It initialises name and active boolean
     * 
     * @param name    It's a name
     * @since         1.0
     * @throws        IllegalArgumentException
     */

    public Group(String name){
        if(name.isEmpty()){
            throw new IllegalArgumentException("Name something");
        }
        this.name=name;
        active=true;
    }

    public Group(BufferedReader br) throws IOException{
        this.name=br.readLine();
        this.active=Boolean.parseBoolean(br.readLine());
    }
    
    public void save(BufferedWriter bw) throws IOException{
        bw.write(name+"\n");
        bw.write(""+active+"\n");
    }

    /**
     * Getter Method which returns the boolean value of active
     * 
     * @since   1.0
     * @return  returns the boolean value of active 
     */
    public boolean isActive(){
        return active;
    }
    
    /**
     * Sets active to boolean value false
     * 
     * @since 1.0
     */
    public void disable(){
        active=false;
    }

    /**
     * Sets active to boolean value true
     * 
     * @since 1.0
     */
    public void enable(){
        active=true;
    }

    /**
     * the toString method to return String name 
     * 
     * @since 1.0
     * @return returns the name or name+[inactive]
     */
    @Override
    public String toString(){
        if(isActive()){
            return name;
        }
        else{
            return name+" [inactive]";
        }
    }
}
