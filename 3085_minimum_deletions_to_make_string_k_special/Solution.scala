// LeetCode 3085 - Minimum Deletions to Make String K-Special
// https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

object Solution {
  def minimumDeletions(word: String, k: Int): Int = {
    val freq = new Array[Int](26)
    var i = 0
    while (i < word.length) {
      freq(word.charAt(i) - 'a') += 1
      i += 1
    }
    val nums = freq.filter(_ > 0)
    var ans = word.length
    i = 0
    while (i <= word.length) {
      var cur = 0
      nums.foreach { x =>
        if (x < i) cur += x
        else if (x > i + k) cur += x - i - k
      }
      ans = math.min(ans, cur)
      i += 1
    }
    ans
  }
}
