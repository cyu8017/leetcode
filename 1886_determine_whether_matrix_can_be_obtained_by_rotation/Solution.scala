// LeetCode 1886 - Determine Whether Matrix Can Be Obtained By Rotation
// https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

object Solution {
  def findRotation(mat: Array[Array[Int]], target: Array[Array[Int]]): Boolean = {
    var current = mat
    for (_ <- 0 until 4) {
      if (current.indices.forall(r => current(r).sameElements(target(r)))) return true
      val n = current.length
      current = Array.tabulate(n, n) { (col, row) => current(n - 1 - row)(col) }
    }
    false
  }
}
