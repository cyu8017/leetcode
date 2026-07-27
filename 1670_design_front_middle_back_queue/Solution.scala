// LeetCode 1670 - Design Front Middle Back Queue
// https://leetcode.com/problems/design-front-middle-back-queue/

class FrontMiddleBackQueue() {
  private val l = scala.collection.mutable.ArrayBuffer[Int]()
  private val r = scala.collection.mutable.ArrayBuffer[Int]()

  private def bal(): Unit = {
    while (l.length > r.length + 1) {
      r.prepend(l.remove(l.length - 1))
    }
    while (r.length > l.length) {
      l += r.remove(0)
    }
  }

  def pushFront(value: Int): Unit = {
    l.prepend(value)
    bal()
  }

  def pushMiddle(value: Int): Unit = {
    if (l.length > r.length) {
      r.prepend(l.remove(l.length - 1))
    }
    l += value
  }

  def pushBack(value: Int): Unit = {
    r += value
    bal()
  }

  def popFront(): Int = {
    if (l.isEmpty) return -1
    val v = l.remove(0)
    bal()
    v
  }

  def popMiddle(): Int = {
    if (l.isEmpty) return -1
    val v = l.remove(l.length - 1)
    bal()
    v
  }

  def popBack(): Int = {
    if (l.isEmpty) return -1
    val v = if (r.nonEmpty) r.remove(r.length - 1) else l.remove(l.length - 1)
    bal()
    v
  }
}
