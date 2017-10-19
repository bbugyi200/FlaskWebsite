package apps;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class TurboEvaluator {
	private static String filename = "vals.txt";
	private static int level;

	public static void main(String[] args) throws IOException {
		try {
			level = Integer.parseInt(args[0]);
		} catch(java.lang.ArrayIndexOutOfBoundsException e) {
			level = 4;
		}

		Test("3", 3);
		Test("a", 5);
		Test("a+b+c", 6);
		Test("a*b-c+(d/e * (a+(b-c)))", 59);
		Test("a/b - d/e + E[F[c+2*F[3]]]", 6.25f);
		Test("a+b/c-2*varx", -6.333333333333f);
		Test("a+b+c-D[e-f] * f + x / varx", -4.2f);
		Test("varx*7+x/(E[c-2*c]-L)", 32.75f);
		Test("(E[x-6]-L)/F[3]", -1.33333333333f);
		Test("x/(E [x-6]-L)/F[3]", -0.75f);
		Test("varx*7+x/(E [x-6]-L)/F[3]", 34.25f);
		Test("a/(b-E[2]) + 77 * varx + F[4]", 393.6428571f);
	}

	private static void Test(String S, float answer) throws IOException {
		Expression expr = new Expression(S);
		expr.buildSymbols();

		if (level == 1) {
			System.out.println("\nTest Expression: " + S);
			expr.printScalars();
			expr.printArrays();
		}

		if (filename != null && !filename.isEmpty()) {
			Scanner scfile = new Scanner(new File(filename));
			expr.loadSymbolValues(scfile);
			if (level == 2 || level == 3) {
				System.out.println("\nTesting Expression on the String: " + S);
				expr.printScalars();
				expr.printArrays();
			}
		}

		if (level < 3) { return; }

		float epsilon = 0.00000001f;
		
		float evaluation = expr.evaluate();
		String result = String.format("evaluate(%s) = %f", S, evaluation);
		String status = Math.abs(evaluation - answer) < epsilon ? "CLEARED" : "FAILED";

		System.out.println(String.format("%-60s%s", result, status));

		if (level < 4) { return; }
	}
}
