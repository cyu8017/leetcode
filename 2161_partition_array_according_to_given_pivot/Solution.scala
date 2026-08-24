// LeetCode 2161 - Partition Array According to Given Pivot
// https://leetcode.com/problems/partition-array-according-to-given-pivot/

object Solution {
  def pivotArray(nums: Array[Int], pivot: Int): Array[Int] = {
    val ans = Array.fill(nums.length)(0)
    var i = 0
    nums.foreach(x => if (x < pivot) { ans(i) = x; i += 1 })
    nums.foreach(x => if (x == pivot) { ans(i) = x; i += 1 })
    nums.foreach(x => if (x > pivot) { ans(i) = x; i += 1 })
    ans
  }
}
