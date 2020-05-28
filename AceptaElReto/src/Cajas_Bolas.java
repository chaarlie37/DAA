import java.util.Scanner;

public class Cajas_Bolas {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()){
            System.out.println(problema(sc.nextInt()));
        }
    }

    public static int problema(int n){
        if (n == 1) {
            return 1;
        }else if(n == 2 || n == 3){
            return 2;
        }else{
            return 2 + problema(n/4);
        }
    }
}