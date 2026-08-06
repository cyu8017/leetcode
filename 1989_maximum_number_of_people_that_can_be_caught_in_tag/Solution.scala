// LeetCode 1989 - Maximum Number of People That Can Be Caught in Tag
// https://leetcode.com/problems/maximum-number-of-people-that-can-be-caught-in-tag/

object Solution {
  def catchMaximumAmountofPeople(team: Array[Int], dist: Int): Int = {
    var ans = 0
    var j = 0
    val n = team.length
    for (i <- team.indices if team(i) == 1) {
      while (j < n && (team(j) == 1 || i - j > dist)) j += 1
      if (j < n && math.abs(i - j) <= dist) {
        ans += 1
        j += 1
      }
    }
    ans
  }
}
