// LeetCode 3717 - Minimum Operations to Make the Array Beautiful
// https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/

object Solution {
  def minOperations(nums: Array[Int]): Int = {
    var f = new java.util.HashMap[Integer, Integer]()
    f.put(nums(0), 0)
    var i = 1
    while (i < nums.length) {
      val x = nums(i)
      val g = new java.util.HashMap[Integer, Integer]()
      val it = f.entrySet().iterator()
      while (it.hasNext) {
        val e = it.next()
        val pre = e.getKey.intValue()
        val s = e.getValue.intValue()
        var cur = (x + pre - 1) / pre * pre
        while (cur <= 100) {
          val `val` = s + (cur - x)
          val old = g.get(cur)
          if (old == null || old > `val`) g.put(cur, `val`)
          cur += pre
        }
      }
      f = g
      i += 1
    }
    var ans = Int.MaxValue
    val vit = f.values().iterator()
    while (vit.hasNext) ans = math.min(ans, vit.next())
    ans
  }
}
