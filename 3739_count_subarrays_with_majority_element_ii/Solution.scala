// LeetCode 3739 - Count Subarrays With Majority Element II
// https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

object Solution {
  private class BIT(n_ : Int) {
    val n: Int = n_
    val c: Array[Int] = new Array[Int](n_ + 1)
    def update(x0: Int, delta: Int): Unit = {
      var x = x0
      while (x <= n) {
        c(x) += delta
        x += x & -x
      }
    }
    def query(x0: Int): Int = {
      var x = x0
      var s = 0
      while (x > 0) {
        s += c(x)
        x -= x & -x
      }
      s
    }
  }

  def countMajoritySubarrays(nums: Array[Int], target: Int): Long = {
    val n = nums.length
    val tree = new BIT(2 * n + 1)
    var s = n + 1
    tree.update(s, 1)
    var ans = 0L
    nums.foreach { x =>
      if (x == target) s += 1 else s -= 1
      ans += tree.query(s - 1)
      tree.update(s, 1)
    }
    ans
  }
}
