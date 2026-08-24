// LeetCode 3751 - Total Waviness Of Numbers In Range I
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

object Solution {
  private def F(x0: Int): Int = {
    var x = x0
    val nums = new java.util.ArrayList[Integer]()
    while (x > 0) {
      nums.add(x % 10)
      x /= 10
    }
    val m = nums.size()
    if (m < 3) return 0
    var s = 0
    var i = 1
    while (i < m - 1) {
      if ((nums.get(i) > nums.get(i - 1) && nums.get(i) > nums.get(i + 1)) ||
          (nums.get(i) < nums.get(i - 1) && nums.get(i) < nums.get(i + 1))) s += 1
      i += 1
    }
    s
  }

  def totalWaviness(num1: Int, num2: Int): Int = {
    var ans = 0
    var x = num1
    while (x <= num2) {
      ans += F(x)
      x += 1
    }
    ans
  }
}
