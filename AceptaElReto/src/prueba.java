import java.util.ArrayList;
import java.util.Arrays;

public class prueba {
    public static void main(String[] args) {
        int [] ps = {15, 10, 4, 19, 9, 16};
        mochila_peso(ps, 30);
    }
    public static void mochila_peso (int[] ps, int c) {
        int[] solParcial = new int[ps.length];
        int[] solOptima = new int[ps.length];
        int pOpt = buscar_peso (ps.length, 0, 0, solParcial, solOptima, -1, ps, c);
        System.out.println(pOpt);
        System.out.println(Arrays.toString(solOptima));
    }
    private static int buscar_peso (int n, int i, int p, int[] solParc,
                                    int[] solOpt, int pOpt,
                                    int[] ps, int c) {
        for (int k=0; k<=1; k++) {
            if (p+k*ps[i]<=c) {
                solParc[i] = k;
                int np = p + k*ps[i];
                if (i==n-1) {
                    if (np>pOpt) {
                        pOpt = np;
                        for (int j=0; j<ps.length; j++)
                            solOpt[j] = solParc[j];
                    }
                }
                else
                    pOpt = buscar_peso (n, i+1, np, solParc, solOpt, pOpt, ps, c);
            }
        }
        return pOpt;
    }
}
