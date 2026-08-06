// LeetCode 1992 - Find All Groups of Farmland
// https://leetcode.com/problems/find-all-groups-of-farmland/

object Solution {
  def findFarmland(land: Array[Array[Int]]): Array[Array[Int]] = {
    val m = land.length
    val n = land(0).length
    val ans = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    for (i <- 0 until m; j <- 0 until n) {
      if (land(i)(j) == 1 && (i == 0 || land(i - 1)(j) == 0) && (j == 0 || land(i)(j - 1) == 0)) {
        var r = i
        var c = j
        while (r + 1 < m && land(r + 1)(j) == 1) r += 1
        while (c + 1 < n && land(i)(c + 1) == 1) c += 1
        ans += Array(i, j, r, c)
      }
    }
    ans.toArray
  }
}
