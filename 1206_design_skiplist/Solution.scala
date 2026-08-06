// LeetCode 1206 - Design Skiplist
// https://leetcode.com/problems/design-skiplist/

class Skiplist() {
  private val values = scala.collection.mutable.ArrayBuffer.empty[Int]

  def search(target: Int): Boolean = {
    val i = lowerBound(target)
    i < values.length && values(i) == target
  }

  def add(num: Int): Unit = {
    val i = lowerBound(num)
    values.insert(i, num)
  }

  def erase(num: Int): Boolean = {
    val i = lowerBound(num)
    if (i == values.length || values(i) != num) false
    else {
      values.remove(i)
      true
    }
  }

  private def lowerBound(x: Int): Int = {
    var lo = 0
    var hi = values.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (values(mid) < x) lo = mid + 1 else hi = mid
    }
    lo
  }
}
