// LeetCode 0948 - Bag of Tokens
// https://leetcode.com/problems/bag-of-tokens/

object Solution {
  def bagOfTokensScore(tokens: Array[Int], power: Int): Int = {
    val arr = tokens.sorted
    var i = 0
    var j = arr.length - 1
    var score = 0
    var ans = 0
    var p = power
    while (i <= j) {
      if (p >= arr(i)) {
        p -= arr(i)
        i += 1
        score += 1
        ans = math.max(ans, score)
      } else if (score > 0) {
        p += arr(j)
        j -= 1
        score -= 1
      } else return ans
    }
    ans
  }
}
