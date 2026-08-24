// LeetCode 3662 - Filter Characters by Frequency
// https://leetcode.com/problems/filter-characters-by-frequency/

object Solution {
  def filterCharacters(s: String, k: Int): String = {
    val cnt = new Array[Int](26)
    for (c <- s) cnt(c - 'a') += 1
    val ans = new StringBuilder
    for (c <- s) if (cnt(c - 'a') < k) ans.append(c)
    ans.toString
  }
}
