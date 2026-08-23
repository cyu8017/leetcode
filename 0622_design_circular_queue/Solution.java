// LeetCode 0622 - Design Circular Queue
// https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue {
    private final int[] data;
    private final int capacity;
    private int head = 0;
    private int size = 0;

    public MyCircularQueue(int k) {
        data = new int[k];
        capacity = k;
    }

    public boolean enQueue(int value) {
        if (isFull()) {
            return false;
        }
        data[(head + size) % capacity] = value;
        ++size;
        return true;
    }

    public boolean deQueue() {
        if (isEmpty()) {
            return false;
        }
        head = (head + 1) % capacity;
        --size;
        return true;
    }

    public int Front() {
        return isEmpty() ? -1 : data[head];
    }

    public int Rear() {
        if (isEmpty()) {
            return -1;
        }
        return data[(head + size - 1) % capacity];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == capacity;
    }
}
