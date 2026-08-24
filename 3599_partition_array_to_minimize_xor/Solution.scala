// LeetCode 3599 - Partition Array to Minimize XOR
// https://leetcode.com/problems/partition-array-to-minimize-xor/

object Solution {
  def minXor(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val g = new Array[Int](n + 1)
    var i = 1
    while (i <= n) { g(i) = g(i - 1) ^ nums(i - 1); i += 1 }
    val Inf = Integer.MAX_VALUE / 2
    val f = Array.fill(n + 1, k + 1)(Inf)
    f(0)(0) = 0
    i = 1
    while (i <= n) {
      var j = 1
      while (j <= math.min(i, k)) {
        var h = j - 1
        while (h < i) {
          f(i)(j) = math.min(f(i)(j), math.max(f(h)(j - 1), g(i) ^ g(h)))
          h += 1
        }
        j += 1
      }
      i += 1
    }
    f(n)(k)
  }
}
