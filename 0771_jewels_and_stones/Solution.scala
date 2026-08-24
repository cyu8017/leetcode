// LeetCode 0771 - Jewels and Stones
// https://leetcode.com/problems/jewels-and-stones/

object Solution {
  def numJewelsInStones(jewels: String, stones: String): Int = {
    val jewelSet = jewels.toSet
    var count = 0
    for (stone <- stones if jewelSet.contains(stone)) count += 1
    count
  }
}
