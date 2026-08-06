// LeetCode 1998 - GCD Sort of an Array
// https://leetcode.com/problems/gcd-sort-of-an-array/

object Solution {
  def gcdSort(nums: Array[Int]): Boolean = {
    val m = nums.max
    val parent = Array.tabulate(m + 1)(identity)

    def find(x0: Int): Int = {
      var x = x0
      while (parent(x) != x) {
        parent(x) = parent(parent(x))
        x = parent(x)
      }
      x
    }

    def union(a: Int, b: Int): Unit = {
      val ra = find(a)
      val rb = find(b)
      if (ra != rb) parent(rb) = ra
    }

    val spf = Array.tabulate(m + 1)(identity)
    var i = 2
    while (i * i <= m) {
      if (spf(i) == i) {
        var j = i * i
        while (j <= m) {
          if (spf(j) == j) spf(j) = i
          j += i
        }
      }
      i += 1
    }

    for (x <- nums.toSet) {
      var y = x
      while (y > 1) {
        val p = spf(y)
        union(x, p)
        while (y % p == 0) y /= p
      }
    }

    val sortedNums = nums.sorted
    nums.indices.forall(i => find(nums(i)) == find(sortedNums(i)))
  }
}
