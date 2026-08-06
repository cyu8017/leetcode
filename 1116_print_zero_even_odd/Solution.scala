// LeetCode 1116 - Print Zero Even Odd
// https://leetcode.com/problems/print-zero-even-odd/

class ZeroEvenOdd(n: Int) {
  private val zeroSem = new java.util.concurrent.Semaphore(1)
  private val evenSem = new java.util.concurrent.Semaphore(0)
  private val oddSem = new java.util.concurrent.Semaphore(0)

  def zero(printNumber: Int => Unit): Unit = {
    for (i <- 0 until n) {
      zeroSem.acquire()
      printNumber(0)
      if (i % 2 == 0) oddSem.release() else evenSem.release()
    }
  }

  def even(printNumber: Int => Unit): Unit = {
    var num = 2
    while (num <= n) {
      evenSem.acquire()
      printNumber(num)
      zeroSem.release()
      num += 2
    }
  }

  def odd(printNumber: Int => Unit): Unit = {
    var num = 1
    while (num <= n) {
      oddSem.acquire()
      printNumber(num)
      zeroSem.release()
      num += 2
    }
  }
}
