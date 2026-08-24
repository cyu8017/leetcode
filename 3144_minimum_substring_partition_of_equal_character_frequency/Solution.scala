// LeetCode 3144 - Minimum Substring Partition of Equal Character Frequency
// https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/

object Solution {
  def minimumSubstringsInPartition(s: String): Int = {
    val n = s.length
    val memo = Array.fill(n)(-1)

    def dfs(i: Int): Int = {
      if (i >= n) return 0
      if (memo(i) != -1) return memo(i)
      val cnt = new Array[Int](26)
      val freq = scala.collection.mutable.Map.empty[Int, Int]
      memo(i) = n - i
      var j = i
      while (j < n) {
        val k = s.charAt(j) - 'a'
        if (cnt(k) > 0) {
          val c = cnt(k)
          val nv = freq(c) - 1
          if (nv == 0) freq.remove(c)
          else freq(c) = nv
        }
        cnt(k) += 1
        freq(cnt(k)) = freq.getOrElse(cnt(k), 0) + 1
        if (freq.size == 1) memo(i) = math.min(memo(i), 1 + dfs(j + 1))
        j += 1
      }
      memo(i)
    }

    dfs(0)
  }
}
