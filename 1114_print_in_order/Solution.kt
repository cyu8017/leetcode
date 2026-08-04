// LeetCode 1114 - Print in Order
// https://leetcode.com/problems/print-in-order/

import java.util.concurrent.Semaphore

class Foo {
    private val second = Semaphore(0)
    private val third = Semaphore(0)

    fun first(printFirst: Runnable) {
        printFirst.run()
        second.release()
    }

    fun second(printSecond: Runnable) {
        second.acquire()
        printSecond.run()
        third.release()
    }

    fun third(printThird: Runnable) {
        third.acquire()
        printThird.run()
    }
}
