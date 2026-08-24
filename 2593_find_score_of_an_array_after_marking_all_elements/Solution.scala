// LeetCode 2593 - Find Score of an Array After Marking All Elements
// https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

object Solution {
  def findScore(nums: Array[Int]): Long = {
    val n = nums.length
    val idx = (0 until n).toArray.sortBy(i => (nums(i), i))
    val marked = Array.fill(n)(false)
    var ans = 0L
    idx.foreach { i =>
      if (!marked(i)) {
        ans += nums(i)
        marked(i) = true
        if (i - 1 >= 0) marked(i - 1) = true
        if (i + 1 < n) marked(i + 1) = true
      }
    }
    ans
  }
}
