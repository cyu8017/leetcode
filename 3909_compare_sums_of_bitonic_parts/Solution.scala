// LeetCode 3909 - Compare Sums Of Bitonic Parts
// https://leetcode.com/problems/compare-sums-of-bitonic-parts/

object Solution {
  def compareBitonicSums(nums: Array[Int]): Int = {
    var l = nums(0).toLong
    var r = 0L
    nums.foreach { x => r += x }
    var i = 1
    var stop = false
    while (i < nums.length && !stop) {
      if (nums(i - 1) > nums(i)) stop = true
      else {
        l += nums(i)
        r -= nums(i - 1)
        i += 1
      }
    }
    if (l == r) -1
    else if (l > r) 0
    else 1
  }
}
