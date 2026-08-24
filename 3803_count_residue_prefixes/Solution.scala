// LeetCode 3803 - Count Residue Prefixes
// https://leetcode.com/problems/count-residue-prefixes/

object Solution {
  def residuePrefixes(s: String): Int = {
    val st = new java.util.HashSet[Character]()
    var ans = 0
    var i = 0
    while (i < s.length) {
      st.add(s.charAt(i))
      if (st.size() == (i + 1) % 3) ans += 1
      i += 1
    }
    ans
  }
}
