// LeetCode 2832 - Maximal Range That Each Element Is Maximum in It
// https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/

object Solution {
  def maximumLength(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val left = Array.fill(n)(0)
    val right = Array.fill(n)(0)
    val st = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (i <- 0 until n) {
      while (st.nonEmpty && nums(st.last) < nums(i)) st.remove(st.length - 1)
      left(i) = if (st.isEmpty) -1 else st.last
      st += i
    }
    st.clear()
    for (i <- n - 1 to 0 by -1) {
      while (st.nonEmpty && nums(st.last) <= nums(i)) st.remove(st.length - 1)
      right(i) = if (st.isEmpty) n else st.last
      st += i
    }
    Array.tabulate(n)(i => right(i) - left(i) - 1)
  }
}
