// LeetCode 1329 - Sort the Matrix Diagonally
// https://leetcode.com/problems/sort-the-matrix-diagonally/

object Solution {
  def diagonalSort(mat: Array[Array[Int]]): Array[Array[Int]] = {
    val diagonals = scala.collection.mutable.HashMap[Int, scala.collection.mutable.ArrayBuffer[Int]]()
    for (r <- mat.indices; c <- mat(r).indices) {
      diagonals.getOrElseUpdate(r - c, scala.collection.mutable.ArrayBuffer[Int]()) += mat(r)(c)
    }
    for (values <- diagonals.values) {
      val sorted = values.sorted(Ordering[Int].reverse)
      values.clear()
      values ++= sorted
    }
    for (r <- mat.indices; c <- mat(r).indices) {
      val buf = diagonals(r - c)
      mat(r)(c) = buf.remove(buf.length - 1)
    }
    mat
  }
}
