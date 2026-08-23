// LeetCode 1670 - Design Front Middle Back Queue
// https://leetcode.com/problems/design-front-middle-back-queue/

using System.Collections.Generic;

public class FrontMiddleBackQueue {
    private readonly LinkedList<int> left = new();
    private readonly LinkedList<int> right = new();

    private void Balance() {
        while (left.Count > right.Count + 1) {
            right.AddFirst(left.Last.Value);
            left.RemoveLast();
        }
        while (right.Count > left.Count) {
            left.AddLast(right.First.Value);
            right.RemoveFirst();
        }
    }

    public void PushFront(int val) {
        left.AddFirst(val);
        Balance();
    }

    public void PushMiddle(int val) {
        if (left.Count > right.Count) {
            right.AddFirst(left.Last.Value);
            left.RemoveLast();
        }
        left.AddLast(val);
    }

    public void PushBack(int val) {
        right.AddLast(val);
        Balance();
    }

    public int PopFront() {
        if (left.Count == 0) return -1;
        int v = left.First.Value;
        left.RemoveFirst();
        Balance();
        return v;
    }

    public int PopMiddle() {
        if (left.Count == 0) return -1;
        int v = left.Last.Value;
        left.RemoveLast();
        Balance();
        return v;
    }

    public int PopBack() {
        if (left.Count == 0) return -1;
        int v;
        if (right.Count > 0) {
            v = right.Last.Value;
            right.RemoveLast();
        } else {
            v = left.Last.Value;
            left.RemoveLast();
        }
        Balance();
        return v;
    }
}
