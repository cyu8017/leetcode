// LeetCode 0544 - Output Contest Matches
// https://leetcode.com/problems/output-contest-matches/

object Solution {
  def findContestMatch(n: Int): String = {
    var teams = (1 to n).map(_.toString).toList
    while (teams.length > 1) {
      val nextRound = teams.indices
        .filter(_ < teams.length / 2)
        .map(i => s"(${teams(i)},${teams(teams.length - 1 - i)})")
        .toList
      teams = nextRound
    }
    teams.head
  }
}
