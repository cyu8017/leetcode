// LeetCode 1816 - Truncate Sentence
// https://leetcode.com/problems/truncate-sentence/

object Solution {
  def truncateSentence(s: String, k: Int): String =
    s.split(" ").take(k).mkString(" ")
}
