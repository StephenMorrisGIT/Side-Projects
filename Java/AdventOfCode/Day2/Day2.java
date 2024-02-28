package Java.AdventOfCode.Day2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Day2 {
    public static void main(String args[]) {
        String filePath = "/Users/stephenmorris/Library/CloudStorage/OneDrive-Personal/stephen.morris/Coding/Side-Projects/Java/AdventOfCode/Day2/input.txt";
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
                // calculate(line);
                System.out.println("Blue = " + checkColor(line, "blue"));
                break;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void calculate(String line) {
        String[] numbers = line.split("\\D+"); // Split the line by non-digit characters
        int sum = 0;
        for (int i = 0; i < numbers.length; i++) { // Exclude the first number
            sum += Integer.parseInt(numbers[i]);
        }
        System.out.println("Sum of numbers: " + sum);
    }

    public static int checkColor(String line, String specificWord) {
        System.out.println(String.format("Line: %s; Word: %s", line, specificWord));
        String[] parts = line.split("\\s+");
        int number = 0;
        for (int i = 0; i < parts.length; i++) {
            if (parts[i].equals(specificWord) && i > 0) {
                number = Integer.parseInt(parts[i - 2]);
                return number;
            }
        }
        System.out.println("Number before " + specificWord + ": " + number);

        return 0;
    }
}
