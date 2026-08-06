// LeetCode 1999 - Smallest Greater Multiple Made of Two Digits
// https://leetcode.com/problems/smallest-greater-multiple-made-of-two-digits/

object Solution {
  def findInteger(k: Int, digit1: Int, digit2: Int): Int = {
    val digits = Set(digit1, digit2).toArray.sorted
    val q = scala.collection.mutable.Queue[Long]()
    val seen = scala.collection.mutable.Set[Long]()
    for (d <- digits if d != 0) {
      q.enqueue(d.toLong)
      seen += d.toLong
    }
    if (q.isEmpty) return -1
    val limit = Int.MaxValue.toLong
    while (q.nonEmpty) {
      val x = q.dequeue()
      if (x > k && x % k == 0) return x.toInt
      for (d <- digits) {
        val nx = x * 10 + d
        if (nx <= limit && !seen.contains(nx)) {
          seen += nx
          q.enqueue(nx)
        }
      }
    }
    -1
  }
}
