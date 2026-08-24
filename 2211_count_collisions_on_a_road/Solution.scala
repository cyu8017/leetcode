// LeetCode 2211 - Count Collisions on a Road
// https://leetcode.com/problems/count-collisions-on-a-road/

object Solution {
  def countCollisions(directions: String): Int = {
    var i = 0
    var j = directions.length - 1
    while (i < directions.length && directions.charAt(i) == 'L') i += 1
    while (j >= 0 && directions.charAt(j) == 'R') j -= 1
    var ans = 0
    var k = i
    while (k <= j) {
      if (directions.charAt(k) != 'S') ans += 1
      k += 1
    }
    ans
  }
}
