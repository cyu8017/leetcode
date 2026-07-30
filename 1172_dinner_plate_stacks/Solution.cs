// LeetCode 1172 - Dinner Plate Stacks
// https://leetcode.com/problems/dinner-plate-stacks/

using System.Collections.Generic;

public class DinnerPlates {
    private readonly int capacity;
    private readonly List<List<int>> stacks = new List<List<int>>();
    private readonly PriorityQueue<int, int> available = new PriorityQueue<int, int>();

    public DinnerPlates(int capacity) {
        this.capacity = capacity;
    }

    public void Push(int val) {
        while (available.Count > 0 &&
               (available.Peek() >= stacks.Count || stacks[available.Peek()].Count == capacity)) {
            available.Dequeue();
        }
        if (available.Count == 0) {
            stacks.Add(new List<int>());
            available.Enqueue(stacks.Count - 1, stacks.Count - 1);
        }
        int idx = available.Peek();
        stacks[idx].Add(val);
        if (stacks[idx].Count == capacity) available.Dequeue();
    }

    public int Pop() {
        while (stacks.Count > 0 && stacks[stacks.Count - 1].Count == 0) stacks.RemoveAt(stacks.Count - 1);
        return stacks.Count == 0 ? -1 : PopAtStack(stacks.Count - 1);
    }

    public int PopAtStack(int index) {
        if (index < 0 || index >= stacks.Count || stacks[index].Count == 0) return -1;
        if (stacks[index].Count == capacity) available.Enqueue(index, index);
        var stack = stacks[index];
        int val = stack[stack.Count - 1];
        stack.RemoveAt(stack.Count - 1);
        return val;
    }
}
