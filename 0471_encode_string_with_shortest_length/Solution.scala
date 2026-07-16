// LeetCode 0471 - Encode String with Shortest Length
// https://leetcode.com/problems/encode-string-with-shortest-length/

object Solution {
  def encode(s: String): String = {
    val length = s.length
    val dp = Array.fill(length + 1)("")

    def encodeWord(word: String): String = {
      val size = word.length
      var best = word
      var unitLength = 1
      while (unitLength <= size / 2) {
        if (size % unitLength == 0) {
          val unit = word.substring(0, unitLength)
          if (unit * (size / unitLength) == word) {
            val encoded = s"${size / unitLength}[$unit]"
            if (encoded.length < best.length || (encoded.length == best.length && encoded < best)) {
              best = encoded
            }
          }
        }
        unitLength += 1
      }
      best
    }

    var index = 1
    while (index <= length) {
      dp(index) = encodeWord(s.substring(0, index))
      var split = 1
      while (split < index) {
        val candidate = dp(index - split) + encodeWord(s.substring(index - split, index))
        if (candidate.length < dp(index).length || (candidate.length == dp(index).length && candidate < dp(index))) {
          dp(index) = candidate
        }
        split += 1
      }
      index += 1
    }
    dp(length)
  }
}
