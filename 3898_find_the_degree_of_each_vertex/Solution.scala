// LeetCode 3898 - Find The Degree Of Each Vertex
// https://leetcode.com/problems/find-the-degree-of-each-vertex/

object Solution {
  def findDegrees(matrix: Array[Array[Int]]): Array[Int] = {
    val ans = new Array[Int](matrix.length)
    var i = 0
    while (i < matrix.length) {
      matrix(i).foreach { x => ans(i) += x }
      i += 1
    }
    ans
  }
}
