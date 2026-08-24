// LeetCode 0952 - Largest Component Size by Common Factor
// https://leetcode.com/problems/largest-component-size-by-common-factor/

object Solution {
  def largestComponentSize(nums: Array[Int]): Int = {
    val mx = nums.max
    val parent = Array.tabulate(mx + 1)(identity)
    def find(x: Int): Int = {
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }
    def unite(a: Int, b: Int): Unit = { parent(find(a)) = find(b) }
    def factors(x0: Int): List[Int] = {
      val res = scala.collection.mutable.ListBuffer[Int]()
      var x = x0
      var d = 2
      while (d.toLong * d <= x) {
        if (x % d == 0) {
          res += d
          while (x % d == 0) x /= d
        }
        d += 1
      }
      if (x > 1) res += x
      res.toList
    }
    nums.foreach { num => factors(num).foreach(f => unite(num, f)) }
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var ans = 0
    nums.foreach { num =>
      val r = find(num)
      val c = cnt.getOrElse(r, 0) + 1
      cnt(r) = c
      ans = math.max(ans, c)
    }
    ans
  }
}
