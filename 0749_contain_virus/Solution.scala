// LeetCode 0749 - Contain Virus
// https://leetcode.com/problems/contain-virus/

object Solution {
  def containVirus(isInfected: Array[Array[Int]]): Int = {
    val m = isInfected.length
    val n = isInfected(0).length
    var walls = 0
    def key(r: Int, c: Int): Long = (r.toLong << 32) | (c.toLong & 0xffffffffL)
    var running = true
    while (running) {
      val seen = scala.collection.mutable.HashSet.empty[Long]
      val regions = scala.collection.mutable.ArrayBuffer.empty[scala.collection.mutable.HashSet[Long]]
      val frontiers = scala.collection.mutable.ArrayBuffer.empty[scala.collection.mutable.HashSet[Long]]
      val perimeters = scala.collection.mutable.ArrayBuffer.empty[Int]
      var i = 0
      while (i < m) {
        var j = 0
        while (j < n) {
          val k = key(i, j)
          if (isInfected(i)(j) == 1 && !seen.contains(k)) {
            val stack = scala.collection.mutable.ArrayBuffer(Array(i, j))
            seen += k
            val region = scala.collection.mutable.HashSet.empty[Long]
            val frontier = scala.collection.mutable.HashSet.empty[Long]
            var perimeter = 0
            val dirs = Array(Array(-1, 0), Array(1, 0), Array(0, -1), Array(0, 1))
            while (stack.nonEmpty) {
              val cur = stack.remove(stack.length - 1)
              val r = cur(0)
              val c = cur(1)
              region += key(r, c)
              for (d <- dirs) {
                val nr = r + d(0)
                val nc = c + d(1)
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                  val nk = key(nr, nc)
                  if (isInfected(nr)(nc) == 1 && seen.add(nk)) stack += Array(nr, nc)
                  else if (isInfected(nr)(nc) == 0) {
                    frontier += nk
                    perimeter += 1
                  }
                }
              }
            }
            regions += region
            frontiers += frontier
            perimeters += perimeter
          }
          j += 1
        }
        i += 1
      }
      if (regions.isEmpty) running = false
      else {
        var quarantine = 0
        var idx = 1
        while (idx < regions.length) {
          if (frontiers(idx).size > frontiers(quarantine).size) quarantine = idx
          idx += 1
        }
        if (frontiers(quarantine).isEmpty) running = false
        else {
          walls += perimeters(quarantine)
          for (cell <- regions(quarantine)) {
            val r = (cell >> 32).toInt
            val c = cell.toInt
            isInfected(r)(c) = -1
          }
          idx = 0
          while (idx < frontiers.length) {
            if (idx != quarantine) {
              for (cell <- frontiers(idx)) {
                val r = (cell >> 32).toInt
                val c = cell.toInt
                isInfected(r)(c) = 1
              }
            }
            idx += 1
          }
        }
      }
    }
    walls
  }
}
