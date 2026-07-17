// LeetCode 1722 - Minimize Hamming Distance After Swap Operations
// https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

object Solution {
  def minimumHammingDistance(source: Array[Int], target: Array[Int], allowedSwaps: Array[Array[Int]]): Int = {
    val n = source.length
    val parent = Array.tabulate(n)(identity)

    def find(start: Int): Int = {
      var x = start
      while (parent(x) != x) {
        parent(x) = parent(parent(x))
        x = parent(x)
      }
      x
    }

    def union(a: Int, b: Int): Unit = {
      val ra = find(a)
      val rb = find(b)
      if (ra != rb) {
        parent(rb) = ra
      }
    }

    allowedSwaps.foreach(swap => union(swap(0), swap(1)))
    val groups = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.Map[Int, Int]]
    for (i <- 0 until n) {
      val counts = groups.getOrElseUpdate(find(i), scala.collection.mutable.Map.empty[Int, Int])
      counts(source(i)) = counts.getOrElse(source(i), 0) + 1
    }
    var ans = 0
    for (i <- 0 until n) {
      val counts = groups(find(i))
      val remaining = counts.getOrElse(target(i), 0)
      if (remaining > 0) {
        counts(target(i)) = remaining - 1
      } else {
        ans += 1
      }
    }
    ans
  }
}
