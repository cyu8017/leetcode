// LeetCode 1996 - The Number of Weak Characters in the Game
// https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

object Solution {
  def numberOfWeakCharacters(properties: Array[Array[Int]]): Int = {
    val sorted = properties.sortBy(x => (x(0), -x(1)))
    var ans = 0
    var maxDef = 0
    for (i <- sorted.length - 1 to 0 by -1) {
      if (sorted(i)(1) < maxDef) ans += 1
      else maxDef = sorted(i)(1)
    }
    ans
  }
}
