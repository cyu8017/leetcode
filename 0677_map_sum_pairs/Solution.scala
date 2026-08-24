// LeetCode 0677 - Map Sum Pairs
// https://leetcode.com/problems/map-sum-pairs/

import scala.collection.mutable

class MapSum() {
  private val values = mutable.Map.empty[String, Int]
  private val prefixSums = mutable.Map.empty[String, Int]

  def insert(key: String, `val`: Int): Unit = {
    val delta = `val` - values.getOrElse(key, 0)
    values(key) = `val`
    var i = 1
    while (i <= key.length) {
      val prefix = key.substring(0, i)
      prefixSums(prefix) = prefixSums.getOrElse(prefix, 0) + delta
      i += 1
    }
  }

  def sum(prefix: String): Int = prefixSums.getOrElse(prefix, 0)
}
