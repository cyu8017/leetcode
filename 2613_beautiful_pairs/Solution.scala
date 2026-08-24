// LeetCode 2613 - Beautiful Pairs
// https://leetcode.com/problems/beautiful-pairs/

object Solution {
  def beautifulPair(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
    val n = nums1.length
    var best = Int.MaxValue
    var ans = Array(0, 1)
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        val d = math.abs(nums1(i) - nums1(j)) + math.abs(nums2(i) - nums2(j))
        if (d < best || (d == best && (i < ans(0) || (i == ans(0) && j < ans(1))))) {
          best = d
          ans = Array(i, j)
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
