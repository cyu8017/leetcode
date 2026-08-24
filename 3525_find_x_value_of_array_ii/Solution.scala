// LeetCode 3525 - Find X Value of Array II
// https://leetcode.com/problems/find-x-value-of-array-ii/

object Solution {
  def resultArray(nums: Array[Int], k: Int, queries: Array[Array[Int]]): Array[Int] = {
    val n = nums.length
    val ans = new Array[Int](queries.length)
    var qi = 0
    while (qi < queries.length) {
      val idx = queries(qi)(0)
      val `val` = queries(qi)(1)
      val start = queries(qi)(2)
      val x = queries(qi)(3)
      nums(idx) = `val`
      var prod = 1
      var cnt = 0
      var i = start
      while (i < n) {
        prod = prod * (nums(i) % k) % k
        if (prod == x) cnt += 1
        i += 1
      }
      ans(qi) = cnt
      qi += 1
    }
    ans
  }
}
