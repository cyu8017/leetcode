// LeetCode 1582 - Special Positions in a Binary Matrix
// https://leetcode.com/problems/special-positions-in-a-binary-matrix/

object Solution {
  def numSpecial(mat: Array[Array[Int]]): Int = {
    val rows = mat.map(_.sum)
    val cols = mat(0).indices.map(j => mat.map(_(j)).sum)
    var ans = 0
    for (i <- mat.indices; j <- mat(0).indices if mat(i)(j) == 1 && rows(i) == 1 && cols(j) == 1) ans += 1
    ans
  }
}
