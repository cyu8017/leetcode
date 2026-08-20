// LeetCode 1188 - Design Bounded Blocking Queue
// https://leetcode.com/problems/design-bounded-blocking-queue/

class BoundedBlockingQueue {
    capacity: any;
    queue: any;

    constructor(capacity: any) {
        this.capacity = capacity;
        this.queue = [];
    }

    enqueue(element: any): any {
        this.queue.push(element);
    }

    dequeue(): any {
        return this.queue.shift();
    }

    size(): any {
        return this.queue.length;
    }
}
