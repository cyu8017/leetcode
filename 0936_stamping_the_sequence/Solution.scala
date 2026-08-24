// LeetCode 0936 - Stamping The Sequence
// https://leetcode.com/problems/stamping-the-sequence/

object Solution {
  def movesToStamp(stamp: String, target: String): Array[Int] = {
    val n = target.length
    val m = stamp.length
    val done = Array.ofDim[Boolean](n)
    val ans = scala.collection.mutable.ArrayBuffer[Int]()
    var changed = true
    while (changed) {
      changed = false
      var i = n - m
      var placed = false
      while (i >= 0 && !placed) {
        var ok = true
        var any = false
        var j = 0
        while (j < m && ok) {
          if (!done(i + j) && target.charAt(i + j) != stamp.charAt(j)) ok = false
          if (!done(i + j)) any = true
          j += 1
        }
        if (ok && any) {
          j = 0
          while (j < m) { done(i + j) = true; j += 1 }
          ans += i
          changed = true
          placed = true
        }
        i -= 1
      }
    }
    if (done.exists(!_)) return Array.empty[Int]
    ans.reverse.toArray
  }
}
