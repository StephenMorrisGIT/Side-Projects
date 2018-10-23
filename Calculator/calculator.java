/*
** This program is designed to perform basic mathematic functions
** (add, subtract, mulitply, divide) in a long fashion.
**
** Designer: Stephen Morris
** Class: Freelance
** Date Created: Thurs, October 18, 2018
** Last Modified: Thurs, October 18, 2018
*/
import java.util.*;

public class calculator{
   public static double[] nums = new double[2];

   public static void main(String[] args){
      // Prints an opening statement so the user know the calculor has started
      System.out.println("Initializing calculator...");
      String choice = userInterface();
      int swtch = 0;
      double result;
      // System.out.println(choice);
      if(choice.equalsIgnoreCase("ADD")){
         swtch = 1;
      }

      switch(swtch){
         case 1:
            result = nums[0] + nums[1];
            System.out.println("Output = " + result);
            break;
      }
   }

   public static String userInterface(){
      System.out.println("What function do you want to perform (Add, Subtract, Mulitply, Divide)?");
      Scanner scan = new Scanner(System.in);
      String func = scan.nextLine();
      System.out.println("Enter your first number");
      nums[0] = (double)(scan.nextInt());
      System.out.println("Enter your second number");
      nums[1] = (double)(scan.nextInt());

      return func;
   }
}
