// LeetCode 0641 - Design Circular Deque
// https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque {
    private final int[] data;
    private final int capacity;
    private int front = 0;
    private int size = 0;

    public MyCircularDeque(int k) {
        data = new int[k];
        capacity = k;
    }

    public boolean insertFront(int value) {
        if (isFull()) {
            return false;
        }
        front = (front - 1 + capacity) % capacity;
        data[front] = value;
        ++size;
        return true;
    }

    public boolean insertLast(int value) {
        if (isFull()) {
            return false;
        }
        data[(front + size) % capacity] = value;
        ++size;
        return true;
    }

    public boolean deleteFront() {
        if (isEmpty()) {
            return false;
        }
        front = (front + 1) % capacity;
        --size;
        return true;
    }

    public boolean deleteLast() {
        if (isEmpty()) {
            return false;
        }
        --size;
        return true;
    }

    public int getFront() {
        return isEmpty() ? -1 : data[front];
    }

    public int getRear() {
        if (isEmpty()) {
            return -1;
        }
        return data[(front + size - 1) % capacity];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == capacity;
    }
}
