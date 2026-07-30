// LeetCode 1188 - Design Bounded Blocking Queue
// https://leetcode.com/problems/design-bounded-blocking-queue/

using System.Collections.Generic;
using System.Threading;

public class BoundedBlockingQueue {
    private readonly int capacity;
    private readonly Queue<int> queue = new Queue<int>();
    private readonly SemaphoreSlim notFull;
    private readonly SemaphoreSlim notEmpty = new SemaphoreSlim(0);
    private readonly object sync = new object();

    public BoundedBlockingQueue(int capacity) {
        this.capacity = capacity;
        notFull = new SemaphoreSlim(capacity);
    }

    public void Enqueue(int element) {
        notFull.Wait();
        lock (sync) {
            queue.Enqueue(element);
        }
        notEmpty.Release();
    }

    public int Dequeue() {
        notEmpty.Wait();
        int value;
        lock (sync) {
            value = queue.Dequeue();
        }
        notFull.Release();
        return value;
    }

    public int Size() {
        lock (sync) {
            return queue.Count;
        }
    }
}
