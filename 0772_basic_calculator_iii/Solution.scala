// LeetCode 0772 - Basic Calculator III
// https://leetcode.com/problems/basic-calculator-iii/

object Solution {
  def calculate(s: String): Int = {
    val expr = s.filter(!_.isWhitespace)
    var i = 0
    def parse(): Int = {
      val stack = scala.collection.mutable.ArrayBuffer.empty[Long]
      var num = 0L
      var sign = '+'
      while (i < expr.length) {
        val ch = expr.charAt(i)
        if (ch.isDigit) num = num * 10 + (ch - '0')
        else if (ch == '(') {
          i += 1
          num = parse().toLong
        }
        if ((!ch.isDigit && ch != '(') || i == expr.length - 1) {
          if (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == ')' || i == expr.length - 1) {
            if (sign == '+') stack += num
            else if (sign == '-') stack += -num
            else if (sign == '*') stack(stack.length - 1) = stack.last * num
            else if (sign == '/') {
              val top = stack.remove(stack.length - 1)
              stack += (top / num.toDouble).toLong
            }
            if (ch == ')') {
              var sum = 0L
              for (v <- stack) sum += v
              return sum.toInt
            }
            sign = ch
            num = 0
          }
        }
        i += 1
      }
      var total = 0L
      for (v <- stack) total += v
      total.toInt
    }
    parse()
  }
}
