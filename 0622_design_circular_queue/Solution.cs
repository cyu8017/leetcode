// LeetCode 0622 - Design Circular Queue
// https://leetcode.com/problems/design-circular-queue/

public class MyCircularQueue {
    private readonly int[] data;
    private readonly int capacity;
    private int head = 0;
    private int size = 0;

    public MyCircularQueue(int k) {
        data = new int[k];
        capacity = k;
    }

    public bool EnQueue(int value) {
        if (IsFull()) return false;
        data[(head + size) % capacity] = value;
        ++size;
        return true;
    }

    public bool DeQueue() {
        if (IsEmpty()) return false;
        head = (head + 1) % capacity;
        --size;
        return true;
    }

    public int Front() => IsEmpty() ? -1 : data[head];

    public int Rear() {
        if (IsEmpty()) return -1;
        return data[(head + size - 1) % capacity];
    }

    public bool IsEmpty() => size == 0;

    public bool IsFull() => size == capacity;
}
