// LeetCode 2726 - Calculator with Method Chaining
// https://leetcode.com/problems/calculator-with-method-chaining/

class Calculator(private var `val`: Double) {
    fun add(v: Double): Calculator {
        `val` += v
        return this
    }

    fun subtract(v: Double): Calculator {
        `val` -= v
        return this
    }

    fun multiply(v: Double): Calculator {
        `val` *= v
        return this
    }

    fun divide(v: Double): Calculator {
        if (v != 0.0) `val` /= v
        return this
    }

    fun power(v: Double): Calculator {
        `val` = Math.pow(`val`, v)
        return this
    }

    fun getResult(): Double = `val`
}

class Solution {
    fun calculatorCreate(`val`: Double): Calculator = Calculator(`val`)
}
