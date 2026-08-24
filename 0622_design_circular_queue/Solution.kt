// LeetCode 0622 - Design Circular Queue
// https://leetcode.com/problems/design-circular-queue/


class MyCircularQueue(k: Int) {
    private val data = IntArray(k)
    private val capacity = k
    private var head = 0
    private var size = 0

    fun enQueue(value: Int): Boolean {
        if (isFull()) return false
        data[(head + size) % capacity] = value
        size++
        return true
    }

    fun deQueue(): Boolean {
        if (isEmpty()) return false
        head = (head + 1) % capacity
        size--
        return true
    }

    fun Front(): Int = if (isEmpty()) -1 else data[head]

    fun Rear(): Int = if (isEmpty()) -1 else data[(head + size - 1) % capacity]

    fun isEmpty(): Boolean = size == 0

    fun isFull(): Boolean = size == capacity
}
