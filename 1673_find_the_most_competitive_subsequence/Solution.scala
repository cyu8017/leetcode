// LeetCode 1673 - Find the Most Competitive Subsequence
// https://leetcode.com/problems/find-the-most-competitive-subsequence/

object Solution {
  def mostCompetitive(nums: Array[Int], k: Int): Array[Int] = {
    val st = scala.collection.mutable.ArrayBuffer[Int]()
    for (i <- nums.indices) {
      val x = nums(i)
      while (st.nonEmpty && st.last > x && st.length - 1 + nums.length - i >= k) {
        st.remove(st.length - 1)
      }
      if (st.length < k) st += x
    }
    st.toArray
  }
}
