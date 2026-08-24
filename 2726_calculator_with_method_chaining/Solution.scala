// LeetCode 2726 - Calculator with Method Chaining
// https://leetcode.com/problems/calculator-with-method-chaining/

class Calculator(private var value: Double) {
  def add(v: Double): Calculator = {
    value += v
    this
  }

  def subtract(v: Double): Calculator = {
    value -= v
    this
  }

  def multiply(v: Double): Calculator = {
    value *= v
    this
  }

  def divide(v: Double): Calculator = {
    if (v != 0) value /= v
    this
  }

  def power(v: Double): Calculator = {
    value = math.pow(value, v)
    this
  }

  def getResult(): Double = value
}

object Solution {
  def calculatorCreate(v: Double): Calculator = new Calculator(v)
}
