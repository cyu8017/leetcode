// LeetCode 0984 - String Without AAA or BBB
// https://leetcode.com/problems/string-without-aaa-or-bbb/

object Solution {
  def strWithout3a3b(a: Int, b: Int): String = {
    val ans = new StringBuilder
    var aa = a
    var bb = b
    while (aa > 0 || bb > 0) {
      val len = ans.length
      val writeA =
        if (len >= 2 && ans.charAt(len - 1) == ans.charAt(len - 2)) ans.charAt(len - 1) == 'b'
        else aa >= bb
      if (writeA) { ans.append('a'); aa -= 1 }
      else { ans.append('b'); bb -= 1 }
    }
    ans.toString
  }
}
