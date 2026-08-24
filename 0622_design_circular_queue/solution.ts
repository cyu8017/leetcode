// LeetCode 0622 - Design Circular Queue
// https://leetcode.com/problems/design-circular-queue/

export class MyCircularQueue {
    constructor(k: number) {
    this.data = Array(k).fill(0);
    this.capacity = k;
    this.head = 0;
    this.size = 0;
}
    enQueue(value: number): boolean {
    if (this.isFull()) return false;
    this.data[(this.head + this.size) % this.capacity] = value;
    ++this.size;
    return true;
}
    deQueue(): boolean {
    if (this.isEmpty()) return false;
    this.head = (this.head + 1) % this.capacity;
    --this.size;
    return true;
}
    Front(): number {
    return this.isEmpty() ? -1 : this.data[this.head];
}
    Rear(): number {
    if (this.isEmpty()) return -1;
    return this.data[(this.head + this.size - 1) % this.capacity];
}
    isEmpty(): boolean {
    return this.size === 0;
}
    isFull(): boolean {
    return this.size === this.capacity;
}
}
