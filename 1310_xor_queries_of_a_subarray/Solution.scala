// LeetCode 1310 - XOR Queries Of A Subarray
// https://leetcode.com/problems/xor-queries-of-a-subarray/

object Solution {
  def xorQueries(arr: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val prefix = Array.ofDim[Int](arr.length + 1)
    for (i <- arr.indices) prefix(i + 1) = prefix(i) ^ arr(i)
    queries.map { q =>
      prefix(q(1) + 1) ^ prefix(q(0))
    }
  }
}
