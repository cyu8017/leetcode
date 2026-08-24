// LeetCode 3551 - Minimum Swaps to Sort by Digit Sum
// https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/

object Solution {
  def f(x0: Int): Int = {
    var x = x0
    var s = 0
    while (x != 0) { s += x % 10; x /= 10 }
    s
  }

  def minSwaps(nums: Array[Int]): Int = {
    val n = nums.length
    val arr = Array.ofDim[Int](n, 2)
    var i = 0
    while (i < n) { arr(i) = Array(f(nums(i)), nums(i)); i += 1 }
    java.util.Arrays.sort(arr, (a: Array[Int], b: Array[Int]) =>
      if (a(0) != b(0)) Integer.compare(a(0), b(0)) else Integer.compare(a(1), b(1)))
    val d = scala.collection.mutable.HashMap.empty[Int, Int]
    i = 0
    while (i < n) { d(arr(i)(1)) = i; i += 1 }
    val vis = new Array[Boolean](n)
    var ans = n
    i = 0
    while (i < n) {
      if (!vis(i)) {
        ans -= 1
        var j = i
        while (!vis(j)) {
          vis(j) = true
          j = d(nums(j))
        }
      }
      i += 1
    }
    ans
  }
}
