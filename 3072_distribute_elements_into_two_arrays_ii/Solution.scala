// LeetCode 3072 - Distribute Elements Into Two Arrays II
// https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/

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

  def resultArray(nums: Array[Int]): Array[Int] = {
    val st = nums.sorted
    val n = st.length
    val tree1 = new BIT(n + 1)
    val tree2 = new BIT(n + 1)
    val arr1 = scala.collection.mutable.ArrayBuffer(nums(0))
    val arr2 = scala.collection.mutable.ArrayBuffer(nums(1))
    tree1.update(idx(st, nums(0)), 1)
    tree2.update(idx(st, nums(1)), 1)
    var i = 2
    while (i < nums.length) {
      val x = nums(i)
      val id = idx(st, x)
      val a = arr1.size - tree1.query(id)
      val b = arr2.size - tree2.query(id)
      if (a > b || (a == b && arr1.size <= arr2.size)) {
        arr1 += x
        tree1.update(id, 1)
      } else {
        arr2 += x
        tree2.update(id, 1)
      }
      i += 1
    }
    (arr1 ++ arr2).toArray
  }

  private def idx(st: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = st.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (st(mid) < x) lo = mid + 1
      else hi = mid
    }
    lo + 1
  }
}
