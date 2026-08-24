// LeetCode 2251 - Number of Flowers in Full Bloom
// https://leetcode.com/problems/number-of-flowers-in-full-bloom/

object Solution {
  def fullBloomFlowers(flowers: Array[Array[Int]], people: Array[Int]): Array[Int] = {
    val start = scala.collection.mutable.ArrayBuffer.empty[Int]
    val end = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (f <- flowers) {
      start += f(0)
      end += f(1)
    }
    val st = start.sorted
    val en = end.sorted
    def upperBound(a: scala.collection.mutable.IndexedSeq[Int], t: Int): Int = {
      var lo = 0
      var hi = a.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (a(mid) <= t) lo = mid + 1 else hi = mid
      }
      lo
    }
    def lowerBound(a: scala.collection.mutable.IndexedSeq[Int], t: Int): Int = {
      var lo = 0
      var hi = a.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (a(mid) < t) lo = mid + 1 else hi = mid
      }
      lo
    }
    val ans = new Array[Int](people.length)
    var i = 0
    while (i < people.length) {
      val t = people(i)
      ans(i) = upperBound(st, t) - lowerBound(en, t)
      i += 1
    }
    ans
  }
}
