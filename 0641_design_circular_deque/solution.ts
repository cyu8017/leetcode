// LeetCode 0641 - Design Circular Deque
// https://leetcode.com/problems/design-circular-deque/

export class MyCircularDeque {
    constructor(k: number) {
    this.data = Array(k).fill(0);
    this.capacity = k;
    this.front = 0;
    this.size = 0;
}
    insertFront(value: number): boolean {
    if (this.isFull()) return false;
    this.front = (this.front - 1 + this.capacity) % this.capacity;
    this.data[this.front] = value;
    ++this.size;
    return true;
}
    insertLast(value: number): boolean {
    if (this.isFull()) return false;
    this.data[(this.front + this.size) % this.capacity] = value;
    ++this.size;
    return true;
}
    deleteFront(): boolean {
    if (this.isEmpty()) return false;
    this.front = (this.front + 1) % this.capacity;
    --this.size;
    return true;
}
    deleteLast(): boolean {
    if (this.isEmpty()) return false;
    --this.size;
    return true;
}
    getFront(): number {
    return this.isEmpty() ? -1 : this.data[this.front];
}
    getRear(): number {
    if (this.isEmpty()) return -1;
    return this.data[(this.front + this.size - 1) % this.capacity];
}
    isEmpty(): boolean {
    return this.size === 0;
}
    isFull(): boolean {
    return this.size === this.capacity;
}
}
