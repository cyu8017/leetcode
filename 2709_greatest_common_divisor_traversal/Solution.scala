// LeetCode 2709 - Greatest Common Divisor Traversal
// https://leetcode.com/problems/greatest-common-divisor-traversal/

object Solution {
  def canTraverseAllPairs(nums: Array[Int]): Boolean = {
    val n = nums.length
    if (n == 1) return true
    var mx = nums(0)
    var i = 0
    while (i < n) {
      if (nums(i) > mx) mx = nums(i)
      i += 1
    }
    val parent = Array.tabulate(mx + 1)(identity)
    val has = new Array[Boolean](mx + 1)
    i = 0
    while (i < n) {
      if (nums(i) == 1) return false
      has(nums(i)) = true
      i += 1
    }

    def find(x0: Int): Int = {
      var x = x0
      while (parent(x) != x) {
        parent(x) = parent(parent(x))
        x = parent(x)
      }
      x
    }

    def unite(a: Int, b: Int): Unit = {
      val ra = find(a)
      val rb = find(b)
      if (ra != rb) parent(ra) = rb
    }

    val sieve = new Array[Int](mx + 1)
    i = 2
    while (i <= mx) {
      if (sieve(i) == 0) {
        var j = i
        while (j <= mx) {
          if (sieve(j) == 0) sieve(j) = i
          if (has(j)) unite(i, j)
          j += i
        }
      }
      i += 1
    }
    val root = find(nums(0))
    i = 0
    while (i < n) {
      if (find(nums(i)) != root) return false
      i += 1
    }
    true
  }
}
