// LeetCode 1115 - Print FooBar Alternately
// https://leetcode.com/problems/print-foobar-alternately/

class FooBar(n: Int) {
  private val fooSem = new java.util.concurrent.Semaphore(1)
  private val barSem = new java.util.concurrent.Semaphore(0)

  def foo(printFoo: Runnable): Unit = {
    for (_ <- 0 until n) {
      fooSem.acquire()
      printFoo.run()
      barSem.release()
    }
  }

  def bar(printBar: Runnable): Unit = {
    for (_ <- 0 until n) {
      barSem.acquire()
      printBar.run()
      fooSem.release()
    }
  }
}
