// LeetCode 3533 - Concatenated Divisibility
// https://leetcode.com/problems/concatenated-divisibility/

object Solution {
  def concatenatedDivisibility(nums0: Array[Int], k: Int): Array[Int] = {
    java.util.Arrays.sort(nums0)
    val nums = nums0
    val n = nums.length
    val pows = new Array[Int](n)
    var i = 0
    while (i < n) {
      var p = 1
      val num = nums(i)
      if (num == 0) p = 10 % k
      else {
        var x = num
        while (x > 0) { p = p * 10 % k; x /= 10 }
      }
      pows(i) = p
      i += 1
    }
    val memo = scala.collection.mutable.HashMap.empty[Long, Boolean]

    def dp(mask: Int, mod: Int): Boolean = {
      if (mask == (1 << n) - 1) return mod == 0
      val key = (mask.toLong << 32) | mod
      if (memo.contains(key)) return memo(key)
      var i = 0
      while (i < n) {
        if (((mask >> i) & 1) == 0) {
          val nm = (mod * pows(i) + nums(i)) % k
          if (dp(mask | (1 << i), nm)) {
            memo(key) = true
            return true
          }
        }
        i += 1
      }
      memo(key) = false
      false
    }

    def reconstruct(mask: Int, mod: Int): java.util.ArrayList[Integer] = {
      var i = 0
      while (i < n) {
        if (((mask >> i) & 1) == 0) {
          val nm = (mod * pows(i) + nums(i)) % k
          if (dp(mask | (1 << i), nm)) {
            val rest = reconstruct(mask | (1 << i), nm)
            rest.add(0, nums(i))
            return rest
          }
        }
        i += 1
      }
      new java.util.ArrayList[Integer]()
    }

    if (!dp(0, 0)) return Array.empty[Int]
    val res = reconstruct(0, 0)
    val out = new Array[Int](res.size())
    var t = 0
    while (t < res.size()) { out(t) = res.get(t); t += 1 }
    out
  }
}
