// LeetCode 0898 - Bitwise ORs of Subarrays
// https://leetcode.com/problems/bitwise-ors-of-subarrays/

object Solution {
  def subarrayBitwiseORs(arr: Array[Int]): Int = {
    val ans = scala.collection.mutable.Set.empty[Int]
    var cur = Set.empty[Int]
    arr.foreach { x =>
      val nxt = scala.collection.mutable.Set(x)
      cur.foreach(y => nxt += (x | y))
      cur = nxt.toSet
      ans ++= cur
    }
    ans.size
  }
}
