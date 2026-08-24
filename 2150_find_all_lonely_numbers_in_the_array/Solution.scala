// LeetCode 2150 - Find All Lonely Numbers in the Array
// https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

object Solution {
  def findLonely(nums: Array[Int]): List[Int] = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    nums.foreach(x => freq(x) = freq.getOrElse(x, 0) + 1)
    freq.collect { case (k, v) if v == 1 && !freq.contains(k - 1) && !freq.contains(k + 1) => k }.toList
  }
}
