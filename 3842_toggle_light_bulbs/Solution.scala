// LeetCode 3842 - Toggle Light Bulbs
// https://leetcode.com/problems/toggle-light-bulbs/

object Solution {
  def toggleLightBulbs(bulbs: Array[Int]): Array[Int] = {
    val st = new Array[Int](101)
    bulbs.foreach { x => st(x) ^= 1 }
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < 101) {
      if (st(i) == 1) ans += i
      i += 1
    }
    ans.toArray
  }
}
