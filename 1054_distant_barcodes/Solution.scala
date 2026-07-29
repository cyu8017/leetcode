// LeetCode 1054 - Distant Barcodes
// https://leetcode.com/problems/distant-barcodes/

object Solution {
  def rearrangeBarcodes(barcodes: Array[Int]): Array[Int] = {
    val count = scala.collection.mutable.Map.empty[Int, Int]
    barcodes.foreach(b => count(b) = count.getOrElse(b, 0) + 1)
    val n = barcodes.length
    val ans = Array.fill(n)(0)
    var i = 0
    count.toSeq.sortBy(-_._2).foreach { case (value, freq) =>
      var f = freq
      while (f > 0) {
        ans(i) = value
        i += 2
        if (i >= n) i = 1
        f -= 1
      }
    }
    ans
  }
}
