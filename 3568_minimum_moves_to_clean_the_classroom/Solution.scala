// LeetCode 3568 - Minimum Moves to Clean the Classroom
// https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

object Solution {
  def minMoves(classroom: Array[String], energy: Int): Int = {
    val m = classroom.length
    val n = classroom(0).length
    val d = Array.ofDim[Int](m, n)
    var x = 0
    var y = 0
    var cnt = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        val c = classroom(i).charAt(j)
        if (c == 'S') { x = i; y = j }
        else if (c == 'L') { d(i)(j) = cnt; cnt += 1 }
        j += 1
      }
      i += 1
    }
    if (cnt == 0) return 0
    val vis = Array.ofDim[Boolean](m, n, energy + 1, 1 << cnt)
    var q = new java.util.ArrayList[Array[Int]]()
    q.add(Array(x, y, energy, (1 << cnt) - 1))
    vis(x)(y)(energy)((1 << cnt) - 1) = true
    val dirs = Array(-1, 0, 1, 0, -1)
    var ans = 0
    while (!q.isEmpty) {
      val t = q
      q = new java.util.ArrayList[Array[Int]]()
      val it = t.iterator()
      while (it.hasNext) {
        val s = it.next()
        i = s(0)
        val j = s(1)
        val curEnergy = s(2)
        val mask = s(3)
        if (mask == 0) return ans
        if (curEnergy > 0) {
          var k = 0
          while (k < 4) {
            val nx = i + dirs(k)
            val ny = j + dirs(k + 1)
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && classroom(nx).charAt(ny) != 'X') {
              val nxtEnergy = if (classroom(nx).charAt(ny) == 'R') energy else curEnergy - 1
              var nxtMask = mask
              if (classroom(nx).charAt(ny) == 'L') nxtMask &= ~(1 << d(nx)(ny))
              if (!vis(nx)(ny)(nxtEnergy)(nxtMask)) {
                vis(nx)(ny)(nxtEnergy)(nxtMask) = true
                q.add(Array(nx, ny, nxtEnergy, nxtMask))
              }
            }
            k += 1
          }
        }
      }
      ans += 1
    }
    -1
  }
}
