// LeetCode 3805 - Count Caesar Cipher Pairs
// https://leetcode.com/problems/count-caesar-cipher-pairs/

object Solution {
  def countPairs(words: Array[String]): Long = {
    val cnt = new java.util.HashMap[String, Integer]()
    words.foreach { word =>
      val s = word.toCharArray
      val k = 'z' - s(0)
      var i = 1
      while (i < s.length) {
        s(i) = ('a' + (s(i) - 'a' + k) % 26).toChar
        i += 1
      }
      s(0) = 'z'
      val key = new String(s)
      if (!cnt.containsKey(key)) cnt.put(key, 0)
      cnt.merge(key, 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
    }
    var ans = 0L
    val it = cnt.values().iterator()
    while (it.hasNext) {
      val v = it.next()
      ans += v.toLong * (v - 1) / 2
    }
    ans
  }
}
