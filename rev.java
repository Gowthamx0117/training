import java.util.Scanner;

class RevString {
    public String reverse(String input) {
        return new StringBuilder(input).reverse().toString();
    }
}

class rev {
    public static void main(String args[]) {
        try (Scanner scanner = new Scanner(System.in)) {
            String ip = scanner.nextLine();
            RevString obj = new RevString();
            String reversed = obj.reverse(ip);
            System.out.println(reversed);
        }
    }
}
