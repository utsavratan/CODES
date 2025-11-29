public class Password {
    public static void validatePassword(String pwd) throws InvalidPasswordException {
        if (pwd == null || pwd.length() < 8 || !pwd.matches(".*\\d.*")) {
            throw new InvalidPasswordException();
        }
    }
    public static void main(String[] args) {
        String[] tests = {"short", "password", "passw0rd", "P4ssw0rd!"};
        for (String p : tests) {
            try {
                validatePassword(p);
                System.out.println(p + " is valid");
            } catch (InvalidPasswordException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}
class InvalidPasswordException extends Exception {
    public InvalidPasswordException() {
        super("Password not strong enough!");
    }
} 