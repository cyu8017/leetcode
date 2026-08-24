// LeetCode 0907 - Sum of Subarray Minimums
// https://leetcode.com/problems/sum-of-subarray-minimums/

object Solution {
  def sumSubarrayMins(arr: Array[Int]): Int = {
    val MOD = 1000000007
    val n = arr.length
    val left = Array.fill(n)(-1)
    val right = Array.fill(n)(n)
    val st = scala.collection.mutable.ArrayDeque[Int]()
    var i = 0
    while (i < n) {
      while (st.nonEmpty && arr(st.last) > arr(i)) st.removeLast()
      left(i) = if (st.isEmpty) -1 else st.last
      st.append(i)
      i += 1
    }
    st.clear()
    i = n - 1
    while (i >= 0) {
      while (st.nonEmpty && arr(st.last) >= arr(i)) st.removeLast()
      right(i) = if (st.isEmpty) n else st.last
      st.append(i)
      i -= 1
    }
    var ans = 0L
    i = 0
    while (i < n) {
      ans = (ans + arr(i).toLong * (i - left(i)) * (right(i) - i)) % MOD
      i += 1
    }
    ans.toInt
  }
}
