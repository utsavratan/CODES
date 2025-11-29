//What is custom Exception and why it is used ?
//

public class InvalidAgeException extends Exception {
    public InvalidAgeException(String m) {
        super(m);
    }
}

class Geeks {
    public static void validate(int age)
    throws InvalidAgeException {
        if (age < 18) {
            throw new InvalidAgeException("Age must be 18 or above");
        } else {
            System.out.println("Valid age: " + age);
        }
    }

        public static void main(String[] args) {
            try {
                validate(12);
            } catch (InvalidAgeException e) {
                System.out.println("Exception caught: " + e.getMessage());
            }
    }
}
