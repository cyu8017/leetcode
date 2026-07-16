// LeetCode 0139 - Word Break
// https://leetcode.com/problems/word-break/

object Solution {
  def wordBreak(s: String, wordDict: List[String]): Boolean = {
    val words = wordDict.toSet
    val dp = Array.fill(s.length + 1)(false)
    dp(0) = true
    for (end <- 1 to s.length; start <- 0 until end if dp(start) && words.contains(s.substring(start, end))) dp(end) = true
    dp(s.length)
  }
}
