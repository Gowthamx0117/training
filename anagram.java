
import java.util.Scanner;

class anagram {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter first string: ");
            String str1 = scanner.nextLine();
            System.out.print("Enter second string: ");
            String str2 = scanner.nextLine();
            
            str1 = str1.replaceAll("\\s","").toLowerCase();
            str2 = str2.replaceAll("\\s", "").toLowerCase();
            
            if (str1.length() != str2.length()) {
                System.out.println("false");
            } else {
                char[] arr1 = str1.toCharArray();
                char[] arr2 = str2.toCharArray();
                java.util.Arrays.sort(arr1);
                java.util.Arrays.sort(arr2);
                if (java.util.Arrays.equals(arr1, arr2)) {
                    System.out.println("true");
                } else {
                    System.out.println("false");
                }
            }
        }
    }
}