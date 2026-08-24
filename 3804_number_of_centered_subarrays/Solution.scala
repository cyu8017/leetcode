// LeetCode 3804 - Number Of Centered Subarrays
// https://leetcode.com/problems/number-of-centered-subarrays/

object Solution {
  def centeredSubarrays(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    var i = 0
    while (i < n) {
      val st = new java.util.HashSet[Integer]()
      var s = 0
      var j = i
      while (j < n) {
        s += nums(j)
        st.add(nums(j))
        if (st.contains(s)) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
