import java.io.Console;

// 
// Decompiled by Procyon v0.6.0
// 

public class main
{
    public static void main(final String[] array) {
        final Console console = System.console();
        System.out.println("How much are you converting?\n");
        final double double1 = Double.parseDouble(console.readLine());
        System.out.println("What would you like to convert to? 1:Euro, 2:Canadian, 3:Yen\n");
        final String line = console.readLine();
        switch (line) {
            case "1": {
                System.out.println(CurrencyConverter.convert_euro(double1));
                break;
            }
            case "2": {
                System.out.println(CurrencyConverter.convert_canada(double1));
                break;
            }
            case "3": {
                System.out.println(CurrencyConverter.convert_yen(double1));
                break;
            }
        }
    }
}
// 
// Decompiled by Procyon v0.6.0
// 

public class CurrencyConverter
{
    public static String convert_euro(final double n) {
        return "Euro: " + n * 0.92;
    }
    
    public static String convert_canada(final double n) {
        return "Canadian: " + n * 1.36;
    }
    
    public static String convert_yen(final double n) {
        return "Japanese Yen: " + n * 145.14;
    }
    
    private static String flag() {
        return "bctf{o0ps_y0u_fOuNd_mE}";
    }
}
