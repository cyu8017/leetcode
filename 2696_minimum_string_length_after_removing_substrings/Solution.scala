// LeetCode 2696 - Minimum String Length After Removing Substrings
// https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

object Solution {
  def minLength(s: String): Int = {
    val st = new StringBuilder
    var i = 0
    while (i < s.length) {
      val c = s.charAt(i)
      val len = st.length
      if (len > 0 && ((st.charAt(len - 1) == 'A' && c == 'B') || (st.charAt(len - 1) == 'C' && c == 'D')))
        st.setLength(len - 1)
      else st.append(c)
      i += 1
    }
    st.length
  }
}
