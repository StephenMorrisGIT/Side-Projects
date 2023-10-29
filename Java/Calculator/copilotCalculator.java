import java.util.Scanner;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class copilotCalculator {
    private static final String LOG_FILE = "calculator.log";

    

    public static void main(String[] args) {
        String userInput = getUserInput();
        log("User input: " + userInput);
    }

    public static String getUserInput() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter input: ");
        String input = scanner.nextLine();
        scanner.close();
        return input;
    }


    public static void log(String message) {
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        String timestamp = now.format(formatter);
        try (PrintWriter out = new PrintWriter(new FileWriter(LOG_FILE, true))) {
            out.print(timestamp + ": ");
            out.println(message);
        } catch (IOException e) {
            System.err.println("Error writing to log file: " + e.getMessage());
        }
    }
}

