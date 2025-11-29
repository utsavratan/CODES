class FinallyExample {
    public static void main(String[] args){

        int[] numbers = {1, 2, 3};
        try {
            System.out.println(numbers[5]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Exception caught: " + e);
        }
        catch (ArithmeticException e) {
            System.out.println("Arithmetic exception caught: " + e);

        } finally {
            System.out.println("This block is always executed.");
        }
        System.out.println("Program continues");
    }
}

/* catch (ArithmeticException e) {
            System.out.println("Error : Division by 0!");
            System.out.println(e);
            e.printStackTrace();
            e.getMessage();
            e.getMessage();
            e.toString();
            e.fillInStackTrace();
            e.getStackTrace();
            for (StackTraceElement element : e.getStackTrace()) {
                System.out.println(element);
            }
                e.getSuppressed();
                for (Throwable t : e.getSuppressed()) {
                    System.out.println(t);
                }
                    System.out.println("End of ArithmeticException handling.");
                    System.out.println();
                    e.printStackTrace();
                    e.getMessage();
                    e.toString();
                    e.fillInStackTrace();
                    e.getStackTrace();
        } */