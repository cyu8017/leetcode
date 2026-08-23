// LeetCode 0225 - Implement Stack using Queues
// https://leetcode.com/problems/implement-stack-using-queues/

using System.Collections.Generic;

public class MyStack {
    private readonly Queue<int> queue = new Queue<int>();

    public void Push(int x) {
        queue.Enqueue(x);
        for (int i = 0; i < queue.Count - 1; i++) {
            queue.Enqueue(queue.Dequeue());
        }
    }

    public int Pop() {
        return queue.Dequeue();
    }

    public int Top() {
        return queue.Peek();
    }

    public bool Empty() {
        return queue.Count == 0;
    }
}
