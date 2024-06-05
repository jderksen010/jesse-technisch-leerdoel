public class Main {
    public static void main(String[] args) {
        Calculator calculator = new Calculator();
        int number1 = 5;
        int number2 = 3;

        int result = calculator.performRandomOperation(number1, number2);
        System.out.println("Result: " + result);
    }
}
