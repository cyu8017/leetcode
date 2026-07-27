// LeetCode 1647 - Minimum Deletions to Make Character Frequencies Unique
// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

object Solution {
  def minDeletions(s: String): Int = {
    val used = scala.collection.mutable.Set.empty[Int]
    var ans = 0
    s.groupBy(identity).values.map(_.length).foreach { freq =>
      var x = freq
      while (x > 0 && used.contains(x)) {
        x -= 1
        ans += 1
      }
      used += x
    }
    ans
  }
}
