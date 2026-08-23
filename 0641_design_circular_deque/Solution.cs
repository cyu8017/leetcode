// LeetCode 0641 - Design Circular Deque
// https://leetcode.com/problems/design-circular-deque/

public class MyCircularDeque {
    private readonly int[] data;
    private readonly int capacity;
    private int front = 0;
    private int size = 0;

    public MyCircularDeque(int k) {
        data = new int[k];
        capacity = k;
    }

    public bool InsertFront(int value) {
        if (IsFull()) return false;
        front = (front - 1 + capacity) % capacity;
        data[front] = value;
        ++size;
        return true;
    }

    public bool InsertLast(int value) {
        if (IsFull()) return false;
        data[(front + size) % capacity] = value;
        ++size;
        return true;
    }

    public bool DeleteFront() {
        if (IsEmpty()) return false;
        front = (front + 1) % capacity;
        --size;
        return true;
    }

    public bool DeleteLast() {
        if (IsEmpty()) return false;
        --size;
        return true;
    }

    public int GetFront() => IsEmpty() ? -1 : data[front];

    public int GetRear() {
        if (IsEmpty()) return -1;
        return data[(front + size - 1) % capacity];
    }

    public bool IsEmpty() => size == 0;

    public bool IsFull() => size == capacity;
}
