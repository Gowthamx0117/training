import java.util.*;

public class atlast {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            // Read input as a single line
            String input = scanner.nextLine();
            // Split by comma and parse to integers
            String[] parts = input.split(",");
            List<Integer> n1 = new ArrayList<>();
            List<Integer> n2 = new ArrayList<>();

            for (String part : parts) {
                int s = Integer.parseInt(part.trim());
                if (s == 0) {
                    n2.add(s);
                } else {
                    n1.add(s);
                }
            }

            Collections.sort(n1);
            List<Integer> result = new ArrayList<>(n1);
            result.addAll(n2);

            System.out.println(result);
        }
    }
}
