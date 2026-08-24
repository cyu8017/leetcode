// LeetCode 3937 - Minimum Operations to Make Array Modulo Alternating I
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/

object Solution {
  def minOperations(nums: Array[Int], k: Int): Int = {
    val a = nums.map(_ % k)
    var ans = Int.MaxValue
    var x = 0
    while (x < k) {
      var y = 0
      while (y < k) {
        if (x != y) {
          var cnt = 0
          var i = 0
          while (i < a.length) {
            val target = if ((i & 1) != 0) y else x
            val diff = math.abs(target - a(i))
            cnt += math.min(diff, k - diff)
            i += 1
          }
          ans = math.min(ans, cnt)
        }
        y += 1
      }
      x += 1
    }
    ans
  }
}
