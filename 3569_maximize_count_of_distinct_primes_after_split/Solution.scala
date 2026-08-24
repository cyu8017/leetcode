// LeetCode 3569 - Maximize Count of Distinct Primes After Split
// https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

object Solution {
  def maximumCount(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    var mx = 0
    for (v <- nums) mx = math.max(mx, v)
    for (q <- queries) mx = math.max(mx, q(1))
    val isP = new Array[Boolean](mx + 1)
    var i = 2
    while (i <= mx) { isP(i) = true; i += 1 }
    i = 2
    while (i * i <= mx) {
      if (isP(i)) {
        var j = i * i
        while (j <= mx) { isP(j) = false; j += i }
      }
      i += 1
    }
    val ans = new Array[Int](queries.length)
    var qi = 0
    while (qi < queries.length) {
      nums(queries(qi)(0)) = queries(qi)(1)
      var best = 0
      val left = scala.collection.mutable.HashMap.empty[Int, Int]
      val right = scala.collection.mutable.HashMap.empty[Int, Int]
      for (v <- nums) if (v <= mx && isP(v)) right(v) = right.getOrElse(v, 0) + 1
      i = 0
      while (i < nums.length - 1) {
        val v = nums(i)
        if (v <= mx && isP(v)) {
          left(v) = left.getOrElse(v, 0) + 1
          val c = right(v) - 1
          if (c == 0) right.remove(v)
          else right(v) = c
        }
        best = math.max(best, left.size + right.size)
        i += 1
      }
      ans(qi) = best
      qi += 1
    }
    ans
  }
}
