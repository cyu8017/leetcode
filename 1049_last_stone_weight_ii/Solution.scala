// LeetCode 1049 - Last Stone Weight II
// https://leetcode.com/problems/last-stone-weight-ii/

object Solution {
  def lastStoneWeightII(stones: Array[Int]): Int = {
    val total = stones.sum
    var reachable = Set(0)
    for (stone <- stones) {
      reachable = reachable.flatMap(s => Set(s + stone, s))
    }
    reachable.map(s => math.abs(total - 2 * s)).min
  }
}
