package JavaCodes;
public class hello {
    public static void main (String [] args){
        System.out.println("help");
        System.out.println(returnNum(4));
    }
    public static int returnNum (int number){
        if(number >= 5){
            return -1;
        } else{
            return 1;
        }
    }
}
