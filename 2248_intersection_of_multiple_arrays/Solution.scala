// LeetCode 2248 - Intersection of Multiple Arrays
// https://leetcode.com/problems/intersection-of-multiple-arrays/

object Solution {
  def intersection(nums: Array[Array[Int]]): List[Int] = {
    val freq = scala.collection.mutable.HashMap.empty[Int, Int]
    for (arr <- nums) {
      val seen = scala.collection.mutable.HashSet.empty[Int]
      for (x <- arr if seen.add(x)) freq(x) = freq.getOrElse(x, 0) + 1
    }
    val ans = scala.collection.mutable.ListBuffer.empty[Int]
    for ((k, v) <- freq if v == nums.length) ans += k
    ans.sorted.toList
  }
}
