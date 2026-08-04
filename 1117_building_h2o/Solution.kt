// LeetCode 1117 - Building H2O
// https://leetcode.com/problems/building-h2o/

import java.util.concurrent.Semaphore

class H2O {
    private val hydrogen = Semaphore(2)
    private val oxygen = Semaphore(0)
    private val lock = Any()
    private var count = 0

    fun hydrogen(releaseHydrogen: Runnable) {
        hydrogen.acquire()
        synchronized(lock) {
            count++
            if (count == 2) oxygen.release()
        }
        releaseHydrogen.run()
    }

    fun oxygen(releaseOxygen: Runnable) {
        oxygen.acquire()
        releaseOxygen.run()
        synchronized(lock) {
            count = 0
            hydrogen.release()
            hydrogen.release()
        }
    }
}
