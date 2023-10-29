public class calculator {
    public static void main(String[] args) {
        String userInput = getUserInput();
        System.out.println("User input: " + userInput);
    }

    public static String getUserInput() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter input: ");
        String input = scanner.nextLine();
        scanner.close();
        return input;
    }
}

