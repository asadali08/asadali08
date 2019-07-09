package HackerRank;

import java.util.Scanner;

public class CountingValleys {
	
	static int countingValleys(int n, String s) {
		int ValleyCounter = 0;
		int altitude = 0;
		
		for(int i = 0; i < n; i++) {
			char ch = s.charAt(i);
			if(ch == 'U') {
				altitude++;
				if(altitude == 0) {
					ValleyCounter++;
				}
			}
			else {
				altitude--;
			}
		}
		return ValleyCounter;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner user = new Scanner(System.in);
		int n = user.nextInt();
		String s = user.next();
		System.out.println(countingValleys(n, s));
		user.close();
	}

}
