// LeetCode 2367 - Number of Arithmetic Triplets
// https://leetcode.com/problems/number-of-arithmetic-triplets/

object Solution {
  def arithmeticTriplets(nums: Array[Int], diff: Int): Int = {
    val seen = scala.collection.mutable.HashSet.empty[Int]
    nums.foreach(x => seen += x)
    var ans = 0
    nums.foreach { x =>
      if (seen.contains(x + diff) && seen.contains(x + 2 * diff)) ans += 1
    }
    ans
  }
}
