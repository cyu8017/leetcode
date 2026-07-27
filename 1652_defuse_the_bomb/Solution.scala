// LeetCode 1652 - Defuse the Bomb
// https://leetcode.com/problems/defuse-the-bomb/

object Solution {
  def decrypt(code: Array[Int], k: Int): Array[Int] = {
    val n = code.length
    val ans = Array.fill(n)(0)
    if (k == 0) return ans
    val a = code ++ code
    for (i <- 0 until n) {
      if (k > 0) {
        var sum = 0
        for (j <- i + 1 to i + k) sum += a(j)
        ans(i) = sum
      } else {
        var sum = 0
        for (j <- i + n + k until i + n) sum += a(j)
        ans(i) = sum
      }
    }
    ans
  }
}
