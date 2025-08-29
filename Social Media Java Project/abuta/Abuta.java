package abuta;

import java.util.List;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

import account.Account;
import message.Group;
import message.Message;
import menu.Menu;
import menu.MenuItem;
import message.Post;


public class Abuta {
    private List<Account> accounts;
    private List<Group> groups;
    private Message message;
    private Menu menu;

    private String output;
    private boolean running=true;
    private String filename="Untitled.abuta";

    public Abuta(){
        accounts= new ArrayList<>();
        accounts.add(new Account("Victor Axelsen"));
        accounts.add(new Account("Lakshay Sen"));
        accounts.add(new Account("HS Prannoy"));
        accounts.add(new Account("Lee Chong Wei"));
        accounts.add(new Account("Lin Dan"));

        groups= new ArrayList<>();
        groups.add(new Group("Birch Forest"));
        groups.add(new Group("Dark Oak"));
        groups.add(new Group("Crimson Forest"));
        groups.add(new Group("Deep Dark"));
        groups.add(new Group("The Badlands"));

        message=new Post(accounts.get(0),groups.get(0),null,"Bellooooo");

        menu=new Menu();
        menu.addMenuItem(new MenuItem("Exit",             () -> endApp()));
        menu.addMenuItem(new MenuItem("Show reply",       ()->showReply()));
        menu.addMenuItem(new MenuItem("Show replied to",  ()->showRepliedTo()));
        menu.addMenuItem(new MenuItem("Add reply",        ()->reply()));
        menu.addMenuItem(new MenuItem("Add Account",      ()->addAccount()));
        menu.addMenuItem(new MenuItem("Add Group",        ()->addGroup()));
        menu.addMenuItem(new MenuItem("New AbUTA",        ()->newAbuta()));
        menu.addMenuItem(new MenuItem("Save",             ()->save()));
        menu.addMenuItem(new MenuItem("Save As",          ()->saveAs()));
        menu.addMenuItem(new MenuItem("Open",             ()->open()));
    }

    private void endApp(){
        running =false;
    }
    
    private void showReply(){
        int num=message.getNumReplies();
        switch(num){
            case 0: output="The message has no replies"; break;
            case 1: message=message.getReply(0); break;
            case 2:
                for(int i=0;i<num;i++){
                    System.out.println(i+" "+message.getReply(i).toString());
                }

                int cho=Menu.getInt("Enter your choice: ");
                if(cho>=0||cho<num){
                    message=message.getReply(cho);
                }
                else{
                    System.out.println("Invalid choice");
                }
                break;
        }
    }
    private void showRepliedTo(){
        if(message.getRepliedTo()==null){
            output="There is no previous reply";
        }
        else{
            message=message.getRepliedTo();
        }
    }

    public void mdi(){
        while(running){
            System.out.println("---------------------Welcome to abUTA--------------------");
            System.out.println(menu);
            System.out.println(output);

            System.out.println("\n".repeat(5));

            menu.run(Menu.getInt("Enter your choice: "));
        }
    }

    private void reply(){
        char temp=Character.toUpperCase(Menu.getChar("(P)Post or (D)Direct Message? "));
        int acc=Menu.selectItemFromList("Account ? ",accounts);
        int gro=Menu.selectItemFromList("Group? ", groups);

        if(temp=='P'){  
            System.out.println("Post from "+accounts.get(acc) + " in "+groups.get(gro)+":");
            System.out.println("----------------------------------------------------");  
            Menu.getString(""); 
            System.out.println("----------------------------------------------------");  
            System.out.println("\n\n");        
        }
        else if(temp=='D'){  
            System.out.println("Message from "+accounts.get(acc) + " in "+groups.get(gro)+":");
            System.out.println("----------------------------------------------------");  
            Menu.getString(""); 
            System.out.println("----------------------------------------------------");  
            System.out.println("\n\n");       
        }
    }

    private void newAbuta(){
        new Abuta();
    }

    private void save(){
        try(BufferedWriter bw=new BufferedWriter(new FileWriter(filename))){
            Message root=message;
            while(root.getRepliedTo()!=null){
                root.getRepliedTo();
            }
            root.save(bw);
            System.out.println("Wrote message to "+filename);
        }
        catch(IOException e){
            e.printStackTrace();
        }
    }

    private void saveAs(){
        String newFileName=Menu.getString("Enter a new file name: ");
        if(newFileName.isEmpty()|| newFileName==null){
            return;
        }
        filename=newFileName;
        save();
    }

    private void open(){
        String newFileName=Menu.getString("Enter a file name to open: ");
        
        if(newFileName.isEmpty()|| newFileName==null){
            return;
        }
        
        filename=newFileName;
        
        try(BufferedReader br=new BufferedReader(new FileReader(filename))){
            message=new Post(br,null);
        }
        catch(IOException e){
            output = "Error opening file: " + e.getMessage();
            e.printStackTrace();
        }

    }

    private void addAccount(){
        accounts.add(new Account(Menu.getString("Enter the account name: ")));
    }

    private void addGroup(){
        groups.add(new Group(Menu.getString("Enter the group name: ")));
    }

    public static void main(String[] args){
        Abuta abuta=new Abuta();
        abuta.mdi();
    }
}
