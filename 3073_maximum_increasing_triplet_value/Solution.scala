// LeetCode 3073 - Maximum Increasing Triplet Value
// https://leetcode.com/problems/maximum-increasing-triplet-value/

object Solution {
  def maximumTripletValue(nums: Array[Int]): Int = {
    val n = nums.length
    val right = new Array[Int](n)
    right(n - 1) = nums(n - 1)
    var i = n - 2
    while (i >= 0) {
      right(i) = math.max(nums(i), right(i + 1))
      i -= 1
    }
    val ts = new java.util.TreeSet[Integer]()
    ts.add(nums(0))
    var ans = 0
    var j = 1
    while (j < n - 1) {
      if (right(j + 1) > nums(j)) {
        val it = ts.lower(nums(j))
        if (it != null) ans = math.max(ans, it - nums(j) + right(j + 1))
      }
      ts.add(nums(j))
      j += 1
    }
    ans
  }
}
