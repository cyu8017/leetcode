// LeetCode 3990 - Create Grid With Exactly K Paths II
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-ii/

object Solution {
  private def bitWidth(k0: Int): Int = {
    var w = 0
    var k = k0
    while (k != 0) {
      w += 1
      k >>= 1
    }
    w
  }

  def createGrid(k0: Int): Array[String] = {
    if (k0 <= 0) return Array.empty[String]
    val l = bitWidth(k0)
    val m = 2 * l
    val n = l + 3
    val result = new Array[String](m)
    var i = 0
    while (i < m) {
      val row = Array.fill(n)('#')
      result(i) = new String(row)
      i += 1
    }
    i = 0
    while (i < l) {
      val r = 2 * i
      val row0 = result(r).toCharArray
      val row1 = result(r + 1).toCharArray
      row0(i) = '.'
      row0(i + 1) = '.'
      row1(i) = '.'
      row1(i + 1) = '.'
      if ((k0 & (1 << i)) != 0) {
        var c = i + 2
        while (c < n) {
          row0(c) = '.'
          c += 1
        }
      }
      result(r) = new String(row0)
      result(r + 1) = new String(row1)
      i += 1
    }
    var r = 0
    while (r < m) {
      val row = result(r).toCharArray
      row(n - 1) = '.'
      result(r) = new String(row)
      r += 1
    }
    result
  }
}
