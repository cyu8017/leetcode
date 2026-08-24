// LeetCode 0985 - Sum of Even Numbers After Queries
// https://leetcode.com/problems/sum-of-even-numbers-after-queries/

object Solution {
  def sumEvenAfterQueries(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    var even = 0
    nums.foreach { x => if (x % 2 == 0) even += x }
    val ans = Array.ofDim[Int](queries.length)
    var qi = 0
    while (qi < queries.length) {
      val value = queries(qi)(0)
      val i = queries(qi)(1)
      if (nums(i) % 2 == 0) even -= nums(i)
      nums(i) += value
      if (nums(i) % 2 == 0) even += nums(i)
      ans(qi) = even
      qi += 1
    }
    ans
  }
}
