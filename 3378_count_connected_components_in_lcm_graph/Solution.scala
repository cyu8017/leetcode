// LeetCode 3378 - Count Connected Components in LCM Graph
// https://leetcode.com/problems/count-connected-components-in-lcm-graph/

object Solution {
  private def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }

  def countComponents(nums: Array[Int], threshold: Int): Int = {
    val n = nums.length
    val parent = Array.tabulate(n)(i => i)
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
    val idx = scala.collection.mutable.HashMap.empty[Int, Int]
    var i = 0
    while (i < n) {
      idx(nums(i)) = i
      i += 1
    }
    var d = 1
    while (d <= threshold) {
      var first = -1
      var m = d
      while (m <= threshold) {
        if (idx.contains(m)) {
          val ii = idx(m)
          if (first == -1) first = ii
          else if (nums(first).toLong * nums(ii) / gcd(nums(first), nums(ii)) <= threshold)
            unite(first, ii)
        }
        m += d
      }
      d += 1
    }
    i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        val a = nums(i)
        val b = nums(j)
        val g = gcd(a, b)
        if (a.toLong / g * b <= threshold) unite(i, j)
        j += 1
      }
      i += 1
    }
    val comp = scala.collection.mutable.HashSet.empty[Int]
    i = 0
    while (i < n) {
      comp += find(i)
      i += 1
    }
    comp.size
  }
}
