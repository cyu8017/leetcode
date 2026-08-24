// LeetCode 3545 - Minimum Deletions for At Most K Distinct Characters
// https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/

object Solution {
  def minDeletion(s: String, k: Int): Int = {
    val cnt = new Array[Int](26)
    for (c <- s.toCharArray) cnt(c - 'a') += 1
    java.util.Arrays.sort(cnt)
    var ans = 0
    var i = 0
    while (i + k < 26) { ans += cnt(i); i += 1 }
    ans
  }
}
