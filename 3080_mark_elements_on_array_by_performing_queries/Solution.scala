// LeetCode 3080 - Mark Elements on Array by Performing Queries
// https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/

object Solution {
  def unmarkedSumArray(nums: Array[Int], queries: Array[Array[Int]]): Array[Long] = {
    val n = nums.length
    var s = 0L
    nums.foreach(x => s += x)
    val mark = new Array[Boolean](n)
    val arr = Array.tabulate(n)(i => Array(nums(i), i))
    scala.util.Sorting.stableSort(arr, (a: Array[Int], b: Array[Int]) =>
      if (a(0) != b(0)) a(0) < b(0) else a(1) < b(1)
    )
    val ans = new Array[Long](queries.length)
    var j = 0
    var qi = 0
    while (qi < queries.length) {
      val index = queries(qi)(0)
      var k = queries(qi)(1)
      if (!mark(index)) {
        mark(index) = true
        s -= nums(index)
      }
      while (k > 0 && j < n) {
        if (!mark(arr(j)(1))) {
          mark(arr(j)(1)) = true
          s -= arr(j)(0)
          k -= 1
        }
        j += 1
      }
      ans(qi) = s
      qi += 1
    }
    ans
  }
}
