// LeetCode 0641 - Design Circular Deque
// https://leetcode.com/problems/design-circular-deque/


class MyCircularDeque(k: Int) {
    private val data = IntArray(k)
    private val capacity = k
    private var head = 0
    private var size = 0

    fun insertFront(value: Int): Boolean {
        if (isFull()) return false
        head = (head - 1 + capacity) % capacity
        data[head] = value
        size++
        return true
    }

    fun insertLast(value: Int): Boolean {
        if (isFull()) return false
        data[(head + size) % capacity] = value
        size++
        return true
    }

    fun deleteFront(): Boolean {
        if (isEmpty()) return false
        head = (head + 1) % capacity
        size--
        return true
    }

    fun deleteLast(): Boolean {
        if (isEmpty()) return false
        size--
        return true
    }

    fun getFront(): Int = if (isEmpty()) -1 else data[head]

    fun getRear(): Int = if (isEmpty()) -1 else data[(head + size - 1) % capacity]

    fun isEmpty(): Boolean = size == 0

    fun isFull(): Boolean = size == capacity
}
