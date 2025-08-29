package message;

public class TestGroup {
    public static void main(String[] args){

        Group g1=new Group("Advitya");
        if(g1.toString().isEmpty()){
            System.err.println("Errorrrrrrr!!!!! The constructor and toString doesn't work");
        }
        else{
            System.err.println("The Contructor and toString works");
        }

        if(g1.isActive()){
            System.err.println("It's active by default");
        }
        else{
            System.err.println("Errrrrrrr!! It's not active by default");
        }

        g1.disable();
        if(g1.isActive()){
            System.err.println("Errrrrrrr!!! It's active after disabling");
        }
        else{
            System.err.println("It's not active after disabling");
        }

        StringBuilder s1=new StringBuilder(g1.toString());
        if(s1.substring(s1.length()-10, s1.length()).equals("[inactive]")){
            System.err.println("inactive is inside the toString return");
        }
        else{
            System.err.println("Errorrrrrr!! inactive is not inside the toString return");
        }

        g1.enable();
        if(g1.isActive()){
            System.err.println("It's active after enabling");
        }
        else{
            System.err.println("Errrrrrrr!!! It's not active after enabling");
        }

    }
}
