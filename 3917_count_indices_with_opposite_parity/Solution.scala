// LeetCode 3917 - Count Indices With Opposite Parity
// https://leetcode.com/problems/count-indices-with-opposite-parity/

object Solution {
  def countOppositeParity(nums: Array[Int]): Array[Int] = {
    val cnt = Array(0, 0)
    nums.foreach { x => cnt(x & 1) += 1 }
    val n = nums.length
    val ans = new Array[Int](n)
    var i = 0
    while (i < n) {
      val x = nums(i)
      cnt(x & 1) -= 1
      ans(i) = cnt((x & 1) ^ 1)
      i += 1
    }
    ans
  }
}
