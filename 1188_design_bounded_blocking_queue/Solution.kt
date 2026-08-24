// LeetCode 1188 - Design Bounded Blocking Queue
// https://leetcode.com/problems/design-bounded-blocking-queue/

import java.util.concurrent.Semaphore

class BoundedBlockingQueue(capacity: Int) {
    private val queue = ArrayDeque<Int>()
    private val notFull = Semaphore(capacity)
    private val notEmpty = Semaphore(0)
    private val lock = Any()

    fun enqueue(element: Int) {
        notFull.acquire()
        synchronized(lock) { queue.addLast(element) }
        notEmpty.release()
    }

    fun dequeue(): Int {
        notEmpty.acquire()
        val value: Int
        synchronized(lock) { value = queue.removeFirst() }
        notFull.release()
        return value
    }

    fun size(): Int = synchronized(lock) { queue.size }
}
