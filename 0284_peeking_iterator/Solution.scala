// LeetCode 0284 - Peeking Iterator
// https://leetcode.com/problems/peeking-iterator/

trait Iterator {
  def next(): Int
  def hasNext(): Boolean
}

class PeekingIterator(iterator: Iterator) {
  private var peeked: Option[Int] = None
  private var hasPeeked = false

  def peek(): Int = {
    if (!hasPeeked) {
      peeked = Some(iterator.next())
      hasPeeked = true
    }
    peeked.get
  }

  def next(): Int = {
    if (hasPeeked) {
      val result = peeked.get
      peeked = None
      hasPeeked = false
      result
    } else {
      iterator.next()
    }
  }

  def hasNext(): Boolean = hasPeeked || iterator.hasNext()
}
