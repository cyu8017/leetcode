// LeetCode 3480 - Maximize Subarrays After Removing One Conflicting Pair
// https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

object Solution {
  def maxSubarrays(n: Int, conflictingPairs: Array[Array[Int]]): Long = {
    val m = conflictingPairs.length
    var best = 0L
    var skip = 0
    while (skip < m) {
      val rightLimit = Array.fill(n + 2)(n + 1)
      var i = 0
      while (i < m) {
        if (i != skip) {
          var a = conflictingPairs(i)(0)
          var b = conflictingPairs(i)(1)
          if (a > b) { val t = a; a = b; b = t }
          if (b < rightLimit(a)) rightLimit(a) = b
        }
        i += 1
      }
      var minRight = n + 1
      var cnt = 0L
      var l = n
      while (l >= 1) {
        if (rightLimit(l) < minRight) minRight = rightLimit(l)
        cnt += minRight - l
        l -= 1
      }
      if (cnt > best) best = cnt
      skip += 1
    }
    best
  }
}
