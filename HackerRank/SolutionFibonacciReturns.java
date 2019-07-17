import java.io.*;
import java.math.*;

public class SolutionFibonacciReturns{
    private BigInteger[] solutions = new BigInteger[100];
    private int maxSolution = 1;
    
    public static void main(String[] args){
        //Enter code here from inputs, print out to outputs
        SolutionFibonacciReturns sol = new SolutionFibonacciReturns();
        //Read input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String number = null;
        int numberInt = 0;
        sol.solutions[0] = BigInteger.ZERO;
        sol.solutions[1] = BigInteger.ONE;
        try{
            while((number = br.readLine()) != null){
                try{
                    numberInt = Integer.parseInt(number);
                    if(numberInt > 100){
                        System.out.println("Error: input number > 100");
                        return;
                    }
                }catch(NumberFormatException e){
                    System.out.println("Error parsing line " + e);
                    return;
                }
                System.out.println(sol.fibonacciIterative(numberInt));
            }
        }catch(IOException e){
            System.out.println("Error reading line " + e);
            return;
        }
    }
    
    public BigInteger fibonacciIterative(int number){
        if(solutions[number] != null)
            return solutions[number];
        for(int i = maxSolution + 1; i <= number; i++){
            solutions[i] = solutions[i - 1].add(solutions[i - 2]);
        }
        maxSolution = number;
        return solutions[number];
    }
}