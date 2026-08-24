// LeetCode 0943 - Find the Shortest Superstring
// https://leetcode.com/problems/find-the-shortest-superstring/

object Solution {
  def shortestSuperstring(words: Array[String]): String = {
    val n = words.length
    val overlap = Array.ofDim[Int](n, n)
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (i != j) {
          val a = words(i)
          val b = words(j)
          var k = math.min(a.length, b.length)
          var found = false
          while (k > 0 && !found) {
            if (a.substring(a.length - k) == b.substring(0, k)) {
              overlap(i)(j) = k
              found = true
            }
            k -= 1
          }
        }
        j += 1
      }
      i += 1
    }
    val N = 1 << n
    val dp = Array.ofDim[String](N, n)
    i = 0
    while (i < n) {
      dp(1 << i)(i) = words(i)
      i += 1
    }
    var mask = 0
    while (mask < N) {
      var last = 0
      while (last < n) {
        if ((mask & (1 << last)) != 0 && dp(mask)(last) != null) {
          var nxt = 0
          while (nxt < n) {
            if ((mask & (1 << nxt)) == 0) {
              val cand = dp(mask)(last) + words(nxt).substring(overlap(last)(nxt))
              val nmask = mask | (1 << nxt)
              if (dp(nmask)(nxt) == null || cand.length < dp(nmask)(nxt).length)
                dp(nmask)(nxt) = cand
            }
            nxt += 1
          }
        }
        last += 1
      }
      mask += 1
    }
    val full = N - 1
    var best: String = null
    i = 0
    while (i < n) {
      if (dp(full)(i) != null && (best == null || dp(full)(i).length < best.length))
        best = dp(full)(i)
      i += 1
    }
    best
  }
}
