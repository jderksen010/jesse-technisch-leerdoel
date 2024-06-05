import static org.junit.jupiter.api.BeforeEach;
import static org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {

    private Calculator calculator;

    @BeforeEach
    void setUp() {
        calculator = new Calculator();
    }

    @Test
    void testSum() {
        int number1 = 5;
        int number2 = 3;
        int expectedResult = 8;
        int actualResult = calculator.sum(number1, number2);
        assertEquals(expectedResult, actualResult);
    }

    @Test
    void testSubtract() {
        int number1 = 10;
        int number2 = 4;
        int expectedResult = 6;
        int actualResult = calculator.subtract(number1, number2);
        assertEquals(expectedResult, actualResult);
    }

    @Test
    void testMultiply() {
        int number1 = 6;
        int number2 = 4;
        int expectedResult = 24;
        int actualResult = calculator.multiply(number1, number2);
        assertEquals(expectedResult, actualResult);
    }

    @Test
    void testDivide() {
        int number1 = 10;
        int number2 = 2;
        int expectedResult = 5;
        int actualResult = calculator.divide(number1, number2);
        assertEquals(expectedResult, actualResult);
    }

    @Test
    void testDivideByZero() {
        assertThrows(ArithmeticException.class, () -> calculator.divide(10, 0));
    }

    @Test
    void testSquare() {
        int number = 5;
        int expectedResult = 25;
        int actualResult = calculator.square(number);
        assertEquals(expectedResult, actualResult);
    }

    @Test
    void testSquareRoot() {
        int number = 16;
        int expectedResult = 4;
        int actualResult = calculator.squareRoot(number);
        assertEquals(expectedResult, actualResult);
    }

    @Test
    void testSquareRootNegative() {
        assertThrows(IllegalArgumentException.class, () -> calculator.squareRoot(-1));
    }

    @Test
    void testCalculatePercentage() {
        int part = 25;
        int whole = 100;
        int expectedResult = 25;
        int actualResult = calculator.calculatePercentage(part, whole);
        assertEquals(expectedResult, actualResult);
    }

    @Test
    void testPerformRandomOperation() {
        int number1 = 10;
        int number2 = 5;

        for (int i = 0; i < 100; i++) {
            int result = calculator.performRandomOperation(number1, number2);
            assertTrue(result >= 0);
        }
    }
}