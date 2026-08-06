// LeetCode 1337 - The K Weakest Rows in a Matrix
// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

object Solution {
  def kWeakestRows(mat: Array[Array[Int]], k: Int): Array[Int] =
    mat.indices.sortBy(i => (mat(i).sum, i)).take(k).toArray
}
