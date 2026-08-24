// LeetCode 2946 - Matrix Similarity After Cyclic Shifts
// https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

object Solution {
  def areSimilar(mat: Array[Array[Int]], k: Int): Boolean = {
    val m = mat.length
    val n = mat(0).length
    var i = 0
    while (i < m) {
      var shift = if (i % 2 == 0) {
        val s = n - (k % n)
        if (s == n) 0 else s
      } else k % n
      var j = 0
      while (j < n) {
        if (mat(i)(j) != mat(i)((j + shift) % n)) return false
        j += 1
      }
      i += 1
    }
    true
  }
}
