// LeetCode 3598 - Longest Common Prefix Between Adjacent Strings After Removals
// https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/

object Solution {
  def calc(s: String, t: String): Int = {
    val m = math.min(s.length, t.length)
    var k = 0
    while (k < m) {
      if (s.charAt(k) != t.charAt(k)) return k
      k += 1
    }
    m
  }

  def longestCommonPrefix(words: Array[String]): Array[Int] = {
    val n = words.length
    val tm = new java.util.TreeMap[Integer, Integer]()

    def add(i: Int, j: Int): Unit = {
      if (i >= 0 && i < n && j >= 0 && j < n)
        tm.merge(calc(words(i), words(j)), 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
    }

    def remove(i: Int, j: Int): Unit = {
      if (i >= 0 && i < n && j >= 0 && j < n) {
        val x = calc(words(i), words(j))
        val c = tm.get(x)
        if (c == 1) tm.remove(x)
        else tm.put(x, c - 1)
      }
    }

    var i = 0
    while (i + 1 < n) { add(i, i + 1); i += 1 }
    val ans = new Array[Int](n)
    i = 0
    while (i < n) {
      remove(i, i + 1)
      remove(i - 1, i)
      add(i - 1, i + 1)
      if (!tm.isEmpty && tm.lastKey() > 0) ans(i) = tm.lastKey()
      remove(i - 1, i + 1)
      add(i - 1, i)
      add(i, i + 1)
      i += 1
    }
    ans
  }
}
