// LeetCode 3731 - Find Missing Elements
// https://leetcode.com/problems/find-missing-elements/

object Solution {
  def findMissingElements(nums: Array[Int]): Array[Int] = {
    var mn = 100
    var mx = 0
    val s = new java.util.HashSet[Integer]()
    nums.foreach { x =>
      mn = math.min(mn, x)
      mx = math.max(mx, x)
      s.add(x)
    }
    val ans = new java.util.ArrayList[Integer]()
    var x = mn + 1
    while (x < mx) {
      if (!s.contains(x)) ans.add(x)
      x += 1
    }
    val out = new Array[Int](ans.size())
    var i = 0
    while (i < out.length) {
      out(i) = ans.get(i)
      i += 1
    }
    out
  }
}
