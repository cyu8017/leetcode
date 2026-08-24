// LeetCode 3272 - Find the Count of Good Integers
// https://leetcode.com/problems/find-the-count-of-good-integers/

object Solution {
  def countGoodIntegers(n: Int, k: Int): Long = {
    val half = (n + 1) / 2
    var start = 1
    var i = 1
    while (i < half) { start *= 10; i += 1 }
    val end = start * 10
    val seen = scala.collection.mutable.HashSet.empty[String]
    var ans = 0L
    val fact = new Array[Long](n + 1)
    fact(0) = 1
    i = 1
    while (i <= n) { fact(i) = fact(i - 1) * i; i += 1 }
    var h = start
    while (h < end) {
      val s = Integer.toString(h)
      val pal = new StringBuilder(s)
      var revStart = s.length - 1
      if (n % 2 == 1) revStart -= 1
      i = revStart
      while (i >= 0) { pal.append(s.charAt(i)); i -= 1 }
      if (pal.toString.toLong % k == 0) {
        val chars = pal.toString.toCharArray
        java.util.Arrays.sort(chars)
        val key = new String(chars)
        if (seen.add(key)) {
          val cnt = new Array[Int](10)
          for (c <- chars) cnt(c - '0') += 1
          var total = fact(n)
          for (c <- cnt) total /= fact(c)
          if (cnt(0) > 0) {
            var bad = fact(n - 1)
            cnt(0) -= 1
            for (c <- cnt) bad /= fact(c)
            cnt(0) += 1
            total -= bad
          }
          ans += total
        }
      }
      h += 1
    }
    ans
  }
}
