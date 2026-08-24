// LeetCode 1115 - Print FooBar Alternately
// https://leetcode.com/problems/print-foobar-alternately/

import java.util.concurrent.Semaphore

class FooBar(private val n: Int) {
    private val fooSem = Semaphore(1)
    private val barSem = Semaphore(0)

    fun foo(printFoo: Runnable) {
        repeat(n) {
            fooSem.acquire()
            printFoo.run()
            barSem.release()
        }
    }

    fun bar(printBar: Runnable) {
        repeat(n) {
            barSem.acquire()
            printBar.run()
            fooSem.release()
        }
    }
}
