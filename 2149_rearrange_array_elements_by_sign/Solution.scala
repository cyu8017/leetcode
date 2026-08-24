// LeetCode 2149 - Rearrange Array Elements by Sign
// https://leetcode.com/problems/rearrange-array-elements-by-sign/

object Solution {
  def rearrangeArray(nums: Array[Int]): Array[Int] = {
    val ans = Array.fill(nums.length)(0)
    var pos = 0
    var neg = 1
    nums.foreach { x =>
      if (x > 0) { ans(pos) = x; pos += 2 }
      else { ans(neg) = x; neg += 2 }
    }
    ans
  }
}
