package com.example;

public class TestMethods {

    // Empty method with a parameter
    public void emptyMethod1(String param) {
    }

    // Another empty method with parameters
    public void emptyMethod2(int a, double b) {
    }

    // Method throwing UnsupportedOperationException with a parameter
    public void unsupportedMethod1(int a, int b) {
        throw new UnsupportedOperationException(reason);
    }

    // Another method throwing UnsupportedOperationException without parameters
    public int unsupportedMethod2(char a) {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    // Normal method
    public String normalMethod1() {
        return "Normal Behavior 1";
    }

    // Another normal method with a parameter
    public int normalMethod2(int value) {
        return value * 2;
    }
}
