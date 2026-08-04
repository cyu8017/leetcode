// LeetCode 1195 - Fizz Buzz Multithreaded
// https://leetcode.com/problems/fizz-buzz-multithreaded/

import java.util.function.IntConsumer

class FizzBuzz(private val n: Int) {
    private var current = 1
    private val lock = Any()

    fun fizz(printFizz: Runnable) = run({ it % 3 == 0 && it % 5 != 0 }, printFizz)
    fun buzz(printBuzz: Runnable) = run({ it % 5 == 0 && it % 3 != 0 }, printBuzz)
    fun fizzbuzz(printFizzBuzz: Runnable) = run({ it % 15 == 0 }, printFizzBuzz)

    fun number(printNumber: IntConsumer) {
        synchronized(lock) {
            while (current <= n) {
                if (current % 3 != 0 && current % 5 != 0) {
                    printNumber.accept(current)
                    current++
                    (lock as Object).notifyAll()
                } else (lock as Object).wait()
            }
        }
    }

    private fun run(pred: (Int) -> Boolean, action: Runnable) {
        synchronized(lock) {
            while (current <= n) {
                if (pred(current)) {
                    action.run()
                    current++
                    (lock as Object).notifyAll()
                } else (lock as Object).wait()
            }
        }
    }
}
