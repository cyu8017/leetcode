// LeetCode 2094 - Finding 3-Digit Even Numbers
// https://leetcode.com/problems/finding-3-digit-even-numbers/

object Solution {
  def findEvenNumbers(digits: Array[Int]): Array[Int] = {
    val freq = Array.fill(10)(0)
    digits.foreach(d => freq(d) += 1)
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    var x = 100
    while (x <= 998) {
      val a = x / 100
      val b = (x / 10) % 10
      val c = x % 10
      freq(a) -= 1; freq(b) -= 1; freq(c) -= 1
      if (freq(a) >= 0 && freq(b) >= 0 && freq(c) >= 0) ans += x
      freq(a) += 1; freq(b) += 1; freq(c) += 1
      x += 2
    }
    ans.toArray
  }
}
