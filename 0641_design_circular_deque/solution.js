// LeetCode 0641 - Design Circular Deque
// https://leetcode.com/problems/design-circular-deque/

/**
 * @param {number} k
 */
var MyCircularDeque = function(k) {
    this.data = Array(k).fill(0);
    this.capacity = k;
    this.front = 0;
    this.size = 0;
};

/**
 * @param {number} value
 * @return {boolean}
 */
MyCircularDeque.prototype.insertFront = function(value) {
    if (this.isFull()) return false;
    this.front = (this.front - 1 + this.capacity) % this.capacity;
    this.data[this.front] = value;
    ++this.size;
    return true;
};

/**
 * @param {number} value
 * @return {boolean}
 */
MyCircularDeque.prototype.insertLast = function(value) {
    if (this.isFull()) return false;
    this.data[(this.front + this.size) % this.capacity] = value;
    ++this.size;
    return true;
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.deleteFront = function() {
    if (this.isEmpty()) return false;
    this.front = (this.front + 1) % this.capacity;
    --this.size;
    return true;
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.deleteLast = function() {
    if (this.isEmpty()) return false;
    --this.size;
    return true;
};

/**
 * @return {number}
 */
MyCircularDeque.prototype.getFront = function() {
    return this.isEmpty() ? -1 : this.data[this.front];
};

/**
 * @return {number}
 */
MyCircularDeque.prototype.getRear = function() {
    if (this.isEmpty()) return -1;
    return this.data[(this.front + this.size - 1) % this.capacity];
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.isEmpty = function() {
    return this.size === 0;
};

/**
 * @return {boolean}
 */
MyCircularDeque.prototype.isFull = function() {
    return this.size === this.capacity;
};
