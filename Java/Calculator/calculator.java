/*
** This program is designed to perform basic mathematic functions
** (add, subtract, mulitply, divide) in a long fashion.
**
** Designer: Stephen Morris
** Class: Freelance
** Date Created: Thurs, October 18, 2018
** Last Modified: Mon, October 29, 2018
*/
import java.util.*;

public class calculator{
   // holds the two operands
   public static double[] nums = new double[2];

   public static void main(String[] args){
      // Prints an opening statement so the user know the calculor has started
      System.out.println("Initializing calculator...");
      String choice = userInterface();
      int swtch = 0; // integer for the switch cases
      double result;
      // System.out.println(choice);
      if(choice.equalsIgnoreCase("ADD") || choice.equalsIgnoreCase("A")){
         swtch = 0;
      }
      else if(choice.equalsIgnoreCase("SUBTRACT") || choice.equalsIgnoreCase("S")){
         swtch = 1;
      }
      else if(choice.equalsIgnoreCase("MULTIPLY") || choice.equalsIgnoreCase("M")){
         swtch = 2;
      }
      else if(choice.equalsIgnoreCase("DIVIDE") || choice.equalsIgnoreCase("D")){
         swtch = 3;
      }

      switch(swtch){
         case 0:
            result = nums[0] + nums[1];
            // System.out.println("Output = " + result);
            printResult(nums[0], nums[1], result);
            break;
         case 1:
            result = nums[0] - nums[1];
            printResult(nums[0], nums[1], result);
            break;
         case 2:
            result = nums[0] * nums[1];
            printResult(nums[0], nums[1], result);
            break;
         case 3:
            result = (nums[0] / nums[1]);
            printResult(nums[0], nums[1], result);
            break;

      }
   }

   public static String userInterface(){
      System.out.println("What function do you want to perform (Add, Subtract, Mulitply, Divide)?");
      // Gets the operation type
      Scanner scan = new Scanner(System.in);
      String func = scan.nextLine();
      // Gets the two operands
      System.out.println("Enter your first number");
      nums[0] = (double)(scan.nextInt());
      System.out.println("Enter your second number");
      nums[1] = (double)(scan.nextInt());

      return func;
   }

   public static void printResult(double a, double b, double c){
      System.out.printf("%f + %f = %f\n", a, b, c);
   }
}
