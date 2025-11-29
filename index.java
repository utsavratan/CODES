import java.util.Scanner;
public class index {
    public static void main(String[] args) {
        int[] a = {10, 20, 30, 40, 50};
        System.out.print("Index (0-" + (a.length - 1) + "): ");
        Scanner s = new Scanner(System.in);
        try {
            int i = s.nextInt();
            if (i >= 0 && i < a.length) System.out.println(a[i]);
            else System.out.println("Invalid index");
        } catch (Exception e) {
            System.out.println("Invalid input");
        } finally {
            s.close();
        }
    }
}
