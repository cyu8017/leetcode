// LeetCode 3289 - The Two Sneaky Numbers of Digitville
// https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

object Solution {
  def getSneakyNumbers(nums: Array[Int]): Array[Int] = {
    val seen = scala.collection.mutable.HashSet.empty[Int]
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (x <- nums) {
      if (!seen.add(x)) ans += x
    }
    ans.toArray
  }
}
