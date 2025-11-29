public class NestedTryExample {
    public static void main(String[] args) {
        try {
            System.out.println("Outer try block");
            try {
                int a = 10 / 0;
            } catch (ArithmeticException e) {
                System.out.println("Inner catch: " + e);
            }
            String str = null;
            System.out.println(str.length());
        } catch (NullPointerException e) {
            System.out.println("Outer catch: " + e);
        }
    }
}

//include Number format exception and array out of bounds exception as well