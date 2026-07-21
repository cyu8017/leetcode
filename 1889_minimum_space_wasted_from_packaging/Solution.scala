// LeetCode 1889 - Minimum Space Wasted From Packaging
// https://leetcode.com/problems/minimum-space-wasted-from-packaging/

object Solution {
  def minWastedSpace(packages: Array[Int], boxes: Array[Array[Int]]): Int = {
    val sortedPackages = packages.sorted
    val prefix = Array.ofDim[Long](sortedPackages.length)
    prefix(0) = sortedPackages(0)
    for (i <- 1 until sortedPackages.length) {
      prefix(i) = prefix(i - 1) + sortedPackages(i)
    }

    var answer = Long.MaxValue
    for (supplier <- boxes) {
      val sortedBoxes = supplier.sorted
      var start = 0
      var wasted = 0L
      var ok = true
      for (box <- sortedBoxes if ok) {
        var lo = start
        var hi = sortedPackages.length
        while (lo < hi) {
          val mid = (lo + hi) / 2
          if (sortedPackages(mid) <= box) lo = mid + 1
          else hi = mid
        }
        val end = lo
        if (end != start) {
          val packageSum = prefix(end - 1) - (if (start > 0) prefix(start - 1) else 0L)
          wasted += box.toLong * (end - start) - packageSum
          start = end
        }
      }
      if (start == sortedPackages.length) {
        answer = math.min(answer, wasted)
      }
    }
    if (answer == Long.MaxValue) -1 else (answer % 1000000007L).toInt
  }
}
