// LeetCode 0922 - Sort Array By Parity II
// https://leetcode.com/problems/sort-array-by-parity-ii/

object Solution {
  def sortArrayByParityII(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val ans = Array.ofDim[Int](n)
    var even = 0
    var odd = 1
    nums.foreach { x =>
      if (x % 2 == 0) { ans(even) = x; even += 2 }
      else { ans(odd) = x; odd += 2 }
    }
    ans
  }
}
