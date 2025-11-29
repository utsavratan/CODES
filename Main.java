//The finally block always executed whether an exception is thrown or not. The finally is used for closing resources like db connections, open files and network connections, It is used after a try-catch block to execute code that must run.

class FinallyExample {
    public static void main(String[] args) {
        int[] numbers = {1,2,3};
        try {
            System.out.println(numbers[5]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Exception cught: " + e);
        } finally {
            System.out.println("Execution of the try-catch block is complete.");
        }
    }
}