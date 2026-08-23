// LeetCode 1188 - Design Bounded Blocking Queue
// https://leetcode.com/problems/design-bounded-blocking-queue/

var BoundedBlockingQueue = function(capacity) {
    this.capacity = capacity;
    this.queue = [];
};

BoundedBlockingQueue.prototype.enqueue = function(element) {
    this.queue.push(element);
};

BoundedBlockingQueue.prototype.dequeue = function() {
    return this.queue.shift();
};

BoundedBlockingQueue.prototype.size = function() {
    return this.queue.length;
};
