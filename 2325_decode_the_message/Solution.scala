// LeetCode 2325 - Decode the Message
// https://leetcode.com/problems/decode-the-message/

object Solution {
  def decodeMessage(key: String, message: String): String = {
    val mp = Array.fill(26)(0.toChar)
    var next = 'a'
    key.foreach { c =>
      if (c != ' ' && mp(c - 'a') == 0) {
        mp(c - 'a') = next
        next = (next + 1).toChar
      }
    }
    val outc = message.toCharArray
    var i = 0
    while (i < outc.length) {
      if (outc(i) != ' ') outc(i) = mp(outc(i) - 'a')
      i += 1
    }
    new String(outc)
  }
}
