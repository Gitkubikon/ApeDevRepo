/*
##############################################################################################
##                                                                                          ##
##   Das ist der Java Code, der sich schon kompiliert in "winkel_berechnung.jar" befindet   ##
##                                                                                          ##
##############################################################################################
*/

package com.nikita.gg;

public class Main {

    public static void main(String[] args) {


    }

/*
##############################################################################################
##                                                                                          ##
##   		Winkel von 2 Vektoren im 2-Dimensionelen Raum berechnen   		    ##
##                                                                                          ##
##############################################################################################
*/

    public static double winkel_zwischen_zwei_vektoren_2d(int vx, int vy, int ux, int uy, double res) {

        int num = (vx * ux + vy * uy);
        double den = (Math.sqrt(Math.pow(vx, 2) + Math.pow(vy, 2)) * (Math.sqrt(Math.pow(ux, 2) + Math.pow(uy, 2))));
        double cos = num / den;
        res = Math.toDegrees(Math.acos(cos));

        return res;

    }
/*
##############################################################################################
##                                                                                          ##
##   		Winkel von 2 Vektoren im 3-Dimensionelen Raum berechnen   		    ##
##                                                                                          ##
##############################################################################################
*/

    public static double winkel_zwischen_zwei_vektoren_3d(int vx, int vy, int vz, int ux, int uy, int uz, double res) {

        int num = (vx * ux + vy * uy + vz * uz);
        double den = (Math.sqrt(Math.pow(vx, 2) + Math.pow(vy, 2)) + Math.pow(vz, 2) * (Math.sqrt(Math.pow(ux, 2) + Math.pow(uy, 2) + Math.pow(uz, 2))));
        double cos = num / den;
        res = Math.toDegrees(Math.acos(cos));

        System.out.println(res);

        return res;

    }
}
