// LeetCode 1505 - Minimum Possible Integer After at Most K Adjacent Swaps On Digits
// https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/

object Solution {
  private class Fenwick(n: Int) {
    private val bit = Array.fill(n + 1)(0)
    def add(i: Int, delta: Int): Unit = {
      var idx = i + 1
      while (idx < bit.length) {
        bit(idx) += delta
        idx += idx & -idx
      }
    }
    def sum(i: Int): Int = {
      var idx = i
      var out = 0
      while (idx > 0) {
        out += bit(idx)
        idx -= idx & -idx
      }
      out
    }
  }

  def minInteger(num: String, k: Int): String = {
    var remaining = k
    val positions = Array.fill(10)(scala.collection.mutable.Queue.empty[Int])
    for (i <- num.indices) positions(num(i) - '0').enqueue(i)
    val fw = new Fenwick(num.length)
    val out = new StringBuilder
    for (_ <- num.indices) {
      var done = false
      var digit = 0
      while (digit < 10 && !done) {
        if (positions(digit).nonEmpty) {
          val index = positions(digit).front
          val cost = index - fw.sum(index)
          if (cost <= remaining) {
            remaining -= cost
            positions(digit).dequeue()
            fw.add(index, 1)
            out.append(('0' + digit).toChar)
            done = true
          }
        }
        digit += 1
      }
    }
    out.toString
  }
}
