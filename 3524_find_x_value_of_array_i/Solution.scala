// LeetCode 3524 - Find X Value of Array I
// https://leetcode.com/problems/find-x-value-of-array-i/

object Solution {
  def resultArray(nums: Array[Int], k: Int): Array[Long] = {
    val ans = new Array[Long](k)
    var dp = new Array[Long](k)
    for (num <- nums) {
      val newDp = new Array[Long](k)
      val nm = num % k
      newDp(nm) = 1
      var i = 0
      while (i < k) { newDp((i * nm) % k) += dp(i); i += 1 }
      i = 0
      while (i < k) { ans(i) += newDp(i); i += 1 }
      dp = newDp
    }
    ans
  }
}
