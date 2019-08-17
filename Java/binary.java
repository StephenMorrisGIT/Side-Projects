/*
** This program is designed to convert 8 bit binary numbers to decimal
** Number of bits could be expanded using for loop in decimalToBinary but the
** number would have to be specified and passed into the loop and the number
** would have to be inside int bounds.
**
** Designer: Stephen Morris
** Class: Freelance
** Date Created: Fri, July 26, 2019
** Last Modified: Fri, August 16, 2019
*/

import java.util.*;

public class binary{
   public static void main(String[] args){
      System.out.println("This program will convert an 8 bit binary number into decimal.");  // Opening message
      int result = binaryToDecimal();
      System.out.print(" = " + result + "\n");  // Print result to screen
   }

   public static int binaryToDecimal(){
      System.out.println("How many digits do you want to convert?");
      Scanner scan = new Scanner(System.in); // Initalize scanner
      int digits = scan.nextInt();  // Take in number of digits

      System.out.println("Enter number with no spaces.");
      int binary = scan.nextInt();// Scan in binary number, reusing 'scan'

      // Makes sure the number is the correct length
         // Need a better way to tell if the number is really just 1's and 0's
      if(binary > (int)Math.pow(10, digits)){
         System.out.println("Number is too large. Please re-enter.");
         binary = scan.nextInt();
      }

      System.out.print(binary);
      int decimal = 0;

      int divisor = 2;  // We will use this number to modulo our binary number and find 1's
      int subtractBinary = 1; // We will subtract this number from our binary number every time the modulo hits
      int addDecimal = 1; // We add this to our decimal number every time the modulo hits

      for(int i = 0; i < digits; i++){
         if((binary % divisor) == subtractBinary){
            decimal += addDecimal;
            binary -= subtractBinary;
         }

         divisor *= 10;
         subtractBinary *= 10;
         addDecimal *= 2;
      }

      /*
      // Checks the 1's place for a 1
      if((binary % 2) == 1){
         decimal += 1;
         binary -= 1;
      }

      if((binary % 20) == 10){
         decimal += 2;
         binary -= 10;
      }

      if((binary % 200) == 100){
         decimal += 4;
         binary -= 100;
      }

      if((binary % 2000) == 1000){
         decimal += 8;
         binary -= 1000;
      }

      if((binary % 20000) == 10000){
         decimal += 16;
         binary -= 10000;
      }

      if((binary % 200000) == 100000){
         decimal += 32;
         binary -= 100000;
      }

      if((binary % 2000000) == 1000000){
         decimal += 64;
         binary -= 1000000;
      }

      if((binary % 20000000) == 10000000){
         decimal += 128;
         binary -= 10000000;
      }
      */

      return decimal;
   }
   /*
   public static String decimalToBinary(){

   }
   */
}
