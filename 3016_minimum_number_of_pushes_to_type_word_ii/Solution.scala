// LeetCode 3016 - Minimum Number of Pushes to Type Word II
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

object Solution {
  def minimumPushes(word: String): Int = {
    val cnt = Array.ofDim[Int](26)
    var i = 0
    while (i < word.length) { cnt(word.charAt(i) - 'a') += 1; i += 1 }
    scala.util.Sorting.quickSort(cnt)
    var ans = 0
    i = 0
    while (i < 26) {
      ans += (i / 8 + 1) * cnt(26 - i - 1)
      i += 1
    }
    ans
  }
}
