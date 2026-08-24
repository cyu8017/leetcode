// LeetCode 3907 - Count Smaller Elements With Opposite Parity
// https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

object Solution {
  private class BIT(n_ : Int) {
    val n = n_
    val c = new Array[Int](n_ + 1)

    def update(x0: Int, delta: Int): Unit = {
      var x = x0
      while (x <= n) {
        c(x) += delta
        x += x & -x
      }
    }

    def query(x0: Int): Int = {
      var s = 0
      var x = x0
      while (x > 0) {
        s += c(x)
        x -= x & -x
      }
      s
    }
  }

  def countSmallerOppositeParity(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val sorted = nums.clone()
    java.util.Arrays.sort(sorted)
    var m = 0
    var i = 0
    while (i < sorted.length) {
      if (i == 0 || sorted(i) != sorted(i - 1)) {
        sorted(m) = sorted(i)
        m += 1
      }
      i += 1
    }
    val uniq = java.util.Arrays.copyOf(sorted, m)
    val bits = Array(new BIT(m), new BIT(m))
    val ans = new Array[Int](n)
    i = n - 1
    while (i >= 0) {
      var x = java.util.Arrays.binarySearch(uniq, nums(i))
      if (x < 0) x = ~x
      x += 1
      ans(i) = bits((nums(i) & 1) ^ 1).query(x - 1)
      bits(nums(i) & 1).update(x, 1)
      i -= 1
    }
    ans
  }
}
