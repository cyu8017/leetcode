// LeetCode 1670 - Design Front Middle Back Queue
// https://leetcode.com/problems/design-front-middle-back-queue/

import java.util.ArrayDeque;
import java.util.Deque;

class FrontMiddleBackQueue {
    private final Deque<Integer> left = new ArrayDeque<>();
    private final Deque<Integer> right = new ArrayDeque<>();

    public FrontMiddleBackQueue() {}

    private void balance() {
        while (left.size() > right.size() + 1) {
            right.addFirst(left.removeLast());
        }
        while (right.size() > left.size()) {
            left.addLast(right.removeFirst());
        }
    }

    public void pushFront(int val) {
        left.addFirst(val);
        balance();
    }

    public void pushMiddle(int val) {
        if (left.size() > right.size()) {
            right.addFirst(left.removeLast());
        }
        left.addLast(val);
    }

    public void pushBack(int val) {
        right.addLast(val);
        balance();
    }

    public int popFront() {
        if (left.isEmpty()) {
            return -1;
        }
        int v = left.removeFirst();
        balance();
        return v;
    }

    public int popMiddle() {
        if (left.isEmpty()) {
            return -1;
        }
        int v = left.removeLast();
        balance();
        return v;
    }

    public int popBack() {
        if (left.isEmpty()) {
            return -1;
        }
        int v = right.isEmpty() ? left.removeLast() : right.removeLast();
        balance();
        return v;
    }
}
