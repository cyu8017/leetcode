// LeetCode 1188 - Design Bounded Blocking Queue
// https://leetcode.com/problems/design-bounded-blocking-queue/

import java.util.*;
import java.util.concurrent.*;

class BoundedBlockingQueue {
    private final int capacity;
    private final Deque<Integer> queue = new ArrayDeque<>();
    private final Semaphore notFull;
    private final Semaphore notEmpty = new Semaphore(0);
    private final Object lock = new Object();

    public BoundedBlockingQueue(int capacity) {
        this.capacity = capacity;
        this.notFull = new Semaphore(capacity);
    }

    public void enqueue(int element) throws InterruptedException {
        notFull.acquire();
        synchronized (lock) { queue.addLast(element); }
        notEmpty.release();
    }

    public int dequeue() throws InterruptedException {
        notEmpty.acquire();
        int value;
        synchronized (lock) { value = queue.removeFirst(); }
        notFull.release();
        return value;
    }

    public int size() {
        synchronized (lock) { return queue.size(); }
    }
}
