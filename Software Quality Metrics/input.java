

public class Example {
    public static void main(String[] args) {
        int result = calculate(5);
        System.out.println(result);
    }

    private static int calculate(int n) {
        return n; // Recursive calls increase depth
    }
}
