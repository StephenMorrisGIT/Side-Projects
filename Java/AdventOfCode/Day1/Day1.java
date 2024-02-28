package Java.AdventOfCode.Day1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Day1 {

        public static void main(String[] args) {
            int lineNumber = 0;

            try {
                BufferedReader reader = new BufferedReader(new FileReader("/Users/stephenmorris/Library/CloudStorage/OneDrive-Personal/stephen.morris/Coding/Side-Projects/Java/AdventOfCode/Day1/input.txt"));
                String line;
                while ((line = reader.readLine()) != null) {
                    lineNumber += calculateCalibration(line);
                    // Process each line of the file here
                    
                }
                reader.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
            System.out.println(lineNumber);
        }
        
        public static int calculateCalibration(String line) {
            // System.out.println(line);
            int lineValue = 0;
            int lineLength = 0;
            Map<String, Integer> charNumbers = new HashMap<>();
            charNumbers.put("one", 1);
            charNumbers.put("two", 2);
            charNumbers.put("three", 3);
            charNumbers.put("four", 4);
            charNumbers.put("five", 5);
            charNumbers.put("six", 6);
            charNumbers.put("seven", 7);
            charNumbers.put("eight", 8);
            charNumbers.put("nine", 9);

            
            lineLength = line.length();
            char[] lineArray = line.toCharArray(); // Create char array from line
            for (String value : charNumbers.keySet()) {
                if(line.startsWith(value)) {
                    lineValue += charNumbers.get(value);
                    break;
                }
            }
            for (int i = 0; i < lineLength; i++) {
                if(lineValue!=0) {
                    break;
                }
                if((int)lineArray[i] > 9 && (int)lineArray[i] >= 48 && (int)lineArray[i] <= 57) {
                   lineValue += lineArray[i];
                    break;
                }
            }


            for (String value : charNumbers.keySet()) {
                if(line.endsWith(value)) {
                    lineValue += charNumbers.get(value);
                    return lineValue;
                }
            }
            for (int i = lineLength - 1; i >= 0; i--) {
                if((int)lineArray[i] > 9 && (int)lineArray[i] >= 48 && (int)lineArray[i] <= 57) {
                    lineValue += lineArray[i];
                    break;
                }
            }

            return lineValue;
        }
    }

