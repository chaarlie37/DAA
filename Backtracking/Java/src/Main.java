public class Main {

    public static void main(String[] args) {
        permutaciones(3);
    }

    public static void permutaciones(int n){
        int[] perm = new int[n];
        boolean[] libres = new boolean[n];

        for (int i = 0; i<n; i++){
            libres[i] = true;
        }

        perms(n, 0, perm, libres);
    }

    public static void imprimir(int[] v){
        for (int i = 0; i<v.length; i++){
            System.out.print(v[i] + " ");
        }
        System.out.println();
    }

    public static void perms(int n, int i, int[] solucion, boolean[] xs){
        for (int k = 0; k < n; k++) {
            if (xs[k]){
                solucion[i] = k;
                xs[k] = false;
                if (i == n-1){
                    imprimir(solucion);
                }else{
                    perms(n, i+1, solucion, xs);
                }
                xs[k] = true;
            }
        }
    }

}
