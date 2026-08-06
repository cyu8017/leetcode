// LeetCode 1188 - Design Bounded Blocking Queue
// https://leetcode.com/problems/design-bounded-blocking-queue/

class BoundedBlockingQueue(capacity: Int) {
  private val queue = new java.util.ArrayDeque[Int]()
  private val notFull = new java.util.concurrent.Semaphore(capacity)
  private val notEmpty = new java.util.concurrent.Semaphore(0)
  private val lock = new Object

  def enqueue(element: Int): Unit = {
    notFull.acquire()
    lock.synchronized { queue.addLast(element) }
    notEmpty.release()
  }

  def dequeue(): Int = {
    notEmpty.acquire()
    val value = lock.synchronized { queue.removeFirst() }
    notFull.release()
    value
  }

  def size(): Int = lock.synchronized { queue.size() }
}
