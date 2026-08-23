// LeetCode 0622 - Design Circular Queue
// https://leetcode.com/problems/design-circular-queue/

/**
 * @param {number} k
 */
var MyCircularQueue = function(k) {
    this.data = Array(k).fill(0);
    this.capacity = k;
    this.head = 0;
    this.size = 0;
};

/**
 * @param {number} value
 * @return {boolean}
 */
MyCircularQueue.prototype.enQueue = function(value) {
    if (this.isFull()) return false;
    this.data[(this.head + this.size) % this.capacity] = value;
    ++this.size;
    return true;
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.deQueue = function() {
    if (this.isEmpty()) return false;
    this.head = (this.head + 1) % this.capacity;
    --this.size;
    return true;
};

/**
 * @return {number}
 */
MyCircularQueue.prototype.Front = function() {
    return this.isEmpty() ? -1 : this.data[this.head];
};

/**
 * @return {number}
 */
MyCircularQueue.prototype.Rear = function() {
    if (this.isEmpty()) return -1;
    return this.data[(this.head + this.size - 1) % this.capacity];
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.isEmpty = function() {
    return this.size === 0;
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.isFull = function() {
    return this.size === this.capacity;
};
