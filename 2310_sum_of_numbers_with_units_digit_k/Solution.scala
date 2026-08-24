// LeetCode 2310 - Sum of Numbers With Units Digit K
// https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/

object Solution {
  def minimumNumbers(num: Int, k: Int): Int = {
    if (num == 0) return 0
    var count = 1
    while (count <= 10) {
      if (count * k % 10 == num % 10 && count * k <= num) return count
      count += 1
    }
    -1
  }
}
