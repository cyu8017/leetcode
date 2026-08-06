// LeetCode 1114 - Print in Order
// https://leetcode.com/problems/print-in-order/

class Foo {
  private val second = new java.util.concurrent.Semaphore(0)
  private val third = new java.util.concurrent.Semaphore(0)

  def first(printFirst: Runnable): Unit = {
    printFirst.run()
    second.release()
  }

  def second(printSecond: Runnable): Unit = {
    second.acquire()
    printSecond.run()
    third.release()
  }

  def third(printThird: Runnable): Unit = {
    third.acquire()
    printThird.run()
  }
}
