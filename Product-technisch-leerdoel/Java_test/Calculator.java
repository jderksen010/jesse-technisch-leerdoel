import java.util.Random;

public class Calculator {

    private int sum(int number1, int number2) {
        return number1 + number2;
    }

    private int subtract(int number1, int number2) {
        return number1 - number2;
    }

    private int multiply(int number1, int number2) {
        return number1 * number2;
    }

    private int divide(int number1, int number2) {
        if (number2 == 0) {
            throw new ArithmeticException("Cannot divide by zero");
        }
        return number1 / number2;
    }

    private int square(int number) {
        return number * number;
    }

    private int squareRoot(int number) {
        if (number < 0) {
            throw new IllegalArgumentException("Cannot calculate square root of a negative number");
        }
        return (int) Math.sqrt(number);
    }

    private int calculatePercentage(int part, int whole) {
        return (int) ((part * 100.0) / whole);
    }

    public int performRandomOperation(int number1, int number2) {
        Random random = new Random();
        int randomIndex = random.nextInt(7);

        switch (randomIndex) {
            case 0:
                return sum(number1, number2);
            case 1:
                return subtract(number1, number2);
            case 2:
                return multiply(number1, number2);
            case 3:
                return divide(number1, number2);
            case 4:
                return square(number1);
            case 5:
                return squareRoot(number1);
            case 6:
                return calculatePercentage(number1, number2);
            default:
                throw new IllegalArgumentException("Invalid random index");
        }
    }
}

