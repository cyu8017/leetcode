// LeetCode 3692 - Majority Frequency Characters
// https://leetcode.com/problems/majority-frequency-characters/

object Solution {
  def majorityFrequencyGroup(s: String): String = {
    val cnt = new Array[Int](26)
    for (c <- s) cnt(c - 'a') += 1
    val f = new java.util.HashMap[Integer, StringBuilder]()
    var i = 0
    while (i < 26) {
      if (cnt(i) > 0)
        f.computeIfAbsent(cnt(i), _ => new StringBuilder).append(('a' + i).toChar)
      i += 1
    }
    var mx = 0
    var mv = 0
    var ans = ""
    val it = f.entrySet().iterator()
    while (it.hasNext) {
      val e = it.next()
      val v = e.getKey.intValue()
      val cs = e.getValue.toString
      if (cs.length > mx || (cs.length == mx && v > mv)) {
        mx = cs.length
        mv = v
        ans = cs
      }
    }
    ans
  }
}
