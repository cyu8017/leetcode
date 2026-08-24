// LeetCode 3458 - Select K Disjoint Special Substrings
// https://leetcode.com/problems/select-k-disjoint-special-substrings/

object Solution {
  def maxSubstringLength(s: String, k: Int): Boolean = {
    val n = s.length
    val first = Array.fill(26)(n)
    val last = Array.fill(26)(-1)
    var i = 0
    while (i < n) {
      val ci = s.charAt(i) - 'a'
      if (first(ci) == n) first(ci) = i
      last(ci) = i
      i += 1
    }
    val segs = new java.util.ArrayList[Array[Int]]()
    var c = 0
    while (c < 26) {
      if (last(c) != -1) {
        var l = first(c)
        var r = last(c)
        i = l
        while (i <= r) {
          val ci = s.charAt(i) - 'a'
          if (first(ci) < l) {
            l = first(ci)
            i = l
          } else {
            if (last(ci) > r) r = last(ci)
            i += 1
          }
        }
        if (!(l == 0 && r == n - 1)) segs.add(Array(l, r))
      }
      c += 1
    }
    val uniq = scala.collection.mutable.Set.empty[Long]
    val arr = new java.util.ArrayList[Array[Int]]()
    val it = segs.iterator()
    while (it.hasNext) {
      val sg = it.next()
      val key = (sg(0).toLong << 32) | (sg(1) & 0xffffffffL)
      if (uniq.add(key)) arr.add(sg)
    }
    arr.sort((a: Array[Int], b: Array[Int]) => java.lang.Integer.compare(a(1), b(1)))
    var cnt = 0
    var end = -1
    val it2 = arr.iterator()
    while (it2.hasNext) {
      val sg = it2.next()
      if (sg(0) > end) {
        cnt += 1
        end = sg(1)
      }
    }
    cnt >= k
  }
}
