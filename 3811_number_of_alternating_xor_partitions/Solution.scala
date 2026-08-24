// LeetCode 3811 - Number Of Alternating Xor Partitions
// https://leetcode.com/problems/number-of-alternating-xor-partitions/

object Solution {
  def alternatingXOR(nums: Array[Int], target1: Int, target2: Int): Int = {
    val MOD = 1000000007
    val cnt1 = new java.util.HashMap[Integer, Integer]()
    val cnt2 = new java.util.HashMap[Integer, Integer]()
    cnt2.put(0, 1)
    var pre = 0
    var ans = 0
    nums.foreach { x =>
      pre ^= x
      val a = cnt2.getOrDefault(pre ^ target1, 0)
      val b = cnt1.getOrDefault(pre ^ target2, 0)
      ans = (a + b) % MOD
      cnt1.merge(pre, a, (x1: Integer, y1: Integer) => Integer.valueOf((x1 + y1) % MOD))
      cnt2.merge(pre, b, (x1: Integer, y1: Integer) => Integer.valueOf((x1 + y1) % MOD))
    }
    ans
  }
}
