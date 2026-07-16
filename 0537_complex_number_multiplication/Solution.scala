// LeetCode 0537 - Complex Number Multiplication
// https://leetcode.com/problems/complex-number-multiplication/

object Solution {
  def complexNumberMultiply(num1: String, num2: String): String = {
    def parse(num: String): (Int, Int) = {
      val parts = num.split("\\+")
      (parts(0).toInt, parts(1).dropRight(1).toInt)
    }

    val (a, b) = parse(num1)
    val (c, d) = parse(num2)
    val real = a * c - b * d
    val imag = a * d + b * c
    s"$real+${imag}i"
  }
}
