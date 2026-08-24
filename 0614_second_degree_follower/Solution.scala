// LeetCode 0614 - Second Degree Follower
// https://leetcode.com/problems/second-degree-follower/

object Solution {
  final val QUERY: String = """SELECT f1.follower, COUNT(DISTINCT f2.follower) AS num
FROM Follow f1
JOIN Follow f2 ON f1.follower = f2.followee
GROUP BY f1.follower
ORDER BY f1.follower
"""
}
