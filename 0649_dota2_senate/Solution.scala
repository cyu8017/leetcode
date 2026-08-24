// LeetCode 0649 - Dota2 Senate
// https://leetcode.com/problems/dota2-senate/

import scala.collection.mutable

object Solution {
  def predictPartyVictory(senate: String): String = {
    val radiant = mutable.Queue.empty[Int]
    val dire = mutable.Queue.empty[Int]
    val n = senate.length
    var i = 0
    while (i < n) {
      if (senate.charAt(i) == 'R') radiant.enqueue(i) else dire.enqueue(i)
      i += 1
    }
    while (radiant.nonEmpty && dire.nonEmpty) {
      val r = radiant.dequeue()
      val d = dire.dequeue()
      if (r < d) radiant.enqueue(r + n) else dire.enqueue(d + n)
    }
    if (radiant.isEmpty) "Dire" else "Radiant"
  }
}
