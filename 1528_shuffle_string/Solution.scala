// LeetCode 1528 - Shuffle String
// https://leetcode.com/problems/shuffle-string/

object Solution {
  def restoreString(s: String, indices: Array[Int]): String = {
    val answer = Array.fill(s.length)(' ')
    for (i <- s.indices) answer(indices(i)) = s(i)
    answer.mkString
  }
}
