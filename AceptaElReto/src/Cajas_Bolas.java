import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Cajas_Bolas {
    public static void main(String[] args) {
        String num = "";
        Scanner sc = new Scanner(System.in);
        do {
            num = sc.nextLine();
            if(!num.equals("")){
                int n = Integer.parseInt(num);
                int[] solucion = new int[n];
                for (int i = 0; i<n; i++){
                    solucion[i] = i+1;
                }
                int[] cajas = new int[n];
                int bolas = (n/2) + 1;
                int viajes = 0;
                while (!compararSoluciones(cajas, solucion) && bolas > 0){
                    for (int i = bolas - 1; i<n; i++){
                        if (cajas[i] + bolas <= i + 1)
                            cajas[i] += bolas;
                    }
                    if(bolas != 1)
                        bolas--;
                    //System.out.println(Arrays.toString(cajas));
                    viajes++;
                }
                System.out.println(viajes);
            }

        }while (!num.equals(""));
    }

    public static boolean compararSoluciones(int[] a1, int[] a2){
        boolean iguales = true;
        int i = 0;
        while (iguales && i < a1.length){
            iguales = a1[i] == a2[i];
            i++;
        }
        return iguales;
    }

}

