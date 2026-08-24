// LeetCode 3102 - Minimize Manhattan Distances
// https://leetcode.com/problems/minimize-manhattan-distances/

object Solution {
  def minimumDistance(points: Array[Array[Int]]): Int = {
    val st1 = new java.util.TreeMap[Integer, Integer]()
    val st2 = new java.util.TreeMap[Integer, Integer]()

    def merge(st: java.util.TreeMap[Integer, Integer], x: Int, v: Int): Unit = {
      val nv = st.getOrDefault(x, 0) + v
      if (nv == 0) st.remove(x)
      else st.put(x, nv)
    }

    points.foreach { p =>
      merge(st1, p(0) + p(1), 1)
      merge(st2, p(0) - p(1), 1)
    }
    var ans = Int.MaxValue
    points.foreach { p =>
      val x = p(0)
      val y = p(1)
      merge(st1, x + y, -1)
      merge(st2, x - y, -1)
      ans = math.min(ans, math.max(st1.lastKey() - st1.firstKey(), st2.lastKey() - st2.firstKey()))
      merge(st1, x + y, 1)
      merge(st2, x - y, 1)
    }
    ans
  }
}
