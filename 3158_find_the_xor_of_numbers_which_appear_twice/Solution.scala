// LeetCode 3158 - Find the XOR of Numbers Which Appear Twice
// https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

object Solution {
  def duplicateNumbersXOR(nums: Array[Int]): Int = {
    val cnt = new Array[Int](51)
    var ans = 0
    nums.foreach { x =>
      cnt(x) += 1
      if (cnt(x) == 2) ans ^= x
    }
    ans
  }
}
