// LeetCode 3769 - Sort Integers By Binary Reflection
// https://leetcode.com/problems/sort-integers-by-binary-reflection/

object Solution {
  def sortByReflection(nums: Array[Int]): Array[Int] = {
    val arr = Array.tabulate[Integer](nums.length)(i => nums(i))
    java.util.Arrays.sort(arr, (a: Integer, b: Integer) => {
      val fa = f(a)
      val fb = f(b)
      if (fa != fb) Integer.compare(fa, fb)
      else Integer.compare(a, b)
    })
    var i = 0
    while (i < nums.length) {
      nums(i) = arr(i)
      i += 1
    }
    nums
  }

  private def f(x0: Int): Int = {
    var x = x0
    var y = 0
    while (x != 0) {
      y = (y << 1) | (x & 1)
      x >>= 1
    }
    y
  }
}
