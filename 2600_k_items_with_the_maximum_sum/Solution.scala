// LeetCode 2600 - K Items With the Maximum Sum
// https://leetcode.com/problems/k-items-with-the-maximum-sum/

object Solution {
  def kItemsWithMaximumSum(numOnes: Int, numZeros: Int, numNegOnes: Int, k0: Int): Int = {
    var k = k0
    var ans = 0
    var take = math.min(numOnes, k)
    ans += take
    k -= take
    take = math.min(numZeros, k)
    k -= take
    take = math.min(numNegOnes, k)
    ans -= take
    ans
  }
}
