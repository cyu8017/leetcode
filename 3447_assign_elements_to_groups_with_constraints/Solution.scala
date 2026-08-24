// LeetCode 3447 - Assign Elements to Groups with Constraints
// https://leetcode.com/problems/assign-elements-to-groups-with-constraints/

object Solution {
  def assignElements(groups: Array[Int], elements: Array[Int]): Array[Int] = {
    val maxV = 100001
    val first = Array.fill(maxV)(-1)
    var i = 0
    while (i < elements.length) {
      val e = elements(i)
      if (e < maxV && first(e) == -1) first(e) = i
      i += 1
    }
    val ans = new Array[Int](groups.length)
    var gi = 0
    while (gi < groups.length) {
      val g = groups(gi)
      var best = -1
      var d = 1
      while (d.toLong * d <= g) {
        if (g % d == 0) {
          if (first(d) != -1 && (best == -1 || first(d) < best)) best = first(d)
          val other = g / d
          if (first(other) != -1 && (best == -1 || first(other) < best)) best = first(other)
        }
        d += 1
      }
      ans(gi) = best
      gi += 1
    }
    ans
  }
}
