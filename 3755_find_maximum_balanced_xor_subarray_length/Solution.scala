// LeetCode 3755 - Find Maximum Balanced Xor Subarray Length
// https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length/

object Solution {
  def maxBalancedSubarray(nums: Array[Int]): Int = {
    val d = new java.util.HashMap[java.lang.Long, Integer]()
    var a = 0
    var b = nums.length
    var ans = 0
    d.put(b.toLong, -1)
    var i = 0
    while (i < nums.length) {
      a ^= nums(i)
      if (nums(i) % 2 == 0) b += 1 else b -= 1
      val key = (a.toLong << 32) | (b & 0xffffffffL)
      if (d.containsKey(key)) ans = math.max(ans, i - d.get(key))
      else d.put(key, i)
      i += 1
    }
    ans
  }
}
