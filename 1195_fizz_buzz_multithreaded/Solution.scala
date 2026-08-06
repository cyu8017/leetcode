// LeetCode 1195 - Fizz Buzz Multithreaded
// https://leetcode.com/problems/fizz-buzz-multithreaded/

class FizzBuzz(n: Int) {
  private var current = 1
  private val lock = new Object

  private def run(predicate: Int => Boolean, action: => Unit): Unit = {
    lock.synchronized {
      while (current <= n) {
        if (predicate(current)) {
          action
          current += 1
          lock.notifyAll()
        } else lock.wait()
      }
    }
  }

  def fizz(printFizz: Runnable): Unit =
    run(x => x % 3 == 0 && x % 5 != 0, printFizz.run())

  def buzz(printBuzz: Runnable): Unit =
    run(x => x % 5 == 0 && x % 3 != 0, printBuzz.run())

  def fizzbuzz(printFizzBuzz: Runnable): Unit =
    run(x => x % 15 == 0, printFizzBuzz.run())

  def number(printNumber: Int => Unit): Unit =
    run(x => x % 3 != 0 && x % 5 != 0, printNumber(current))
}
