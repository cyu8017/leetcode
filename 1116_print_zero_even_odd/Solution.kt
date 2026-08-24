// LeetCode 1116 - Print Zero Even Odd
// https://leetcode.com/problems/print-zero-even-odd/

import java.util.concurrent.Semaphore
import java.util.function.IntConsumer

class ZeroEvenOdd(private val n: Int) {
    private val zeroSem = Semaphore(1)
    private val evenSem = Semaphore(0)
    private val oddSem = Semaphore(0)

    fun zero(printNumber: IntConsumer) {
        for (i in 0 until n) {
            zeroSem.acquire()
            printNumber.accept(0)
            if (i % 2 == 0) oddSem.release() else evenSem.release()
        }
    }

    fun even(printNumber: IntConsumer) {
        var num = 2
        while (num <= n) {
            evenSem.acquire()
            printNumber.accept(num)
            zeroSem.release()
            num += 2
        }
    }

    fun odd(printNumber: IntConsumer) {
        var num = 1
        while (num <= n) {
            oddSem.acquire()
            printNumber.accept(num)
            zeroSem.release()
            num += 2
        }
    }
}
