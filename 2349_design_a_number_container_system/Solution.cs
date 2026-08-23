// LeetCode 2349 - Design a Number Container System
// https://leetcode.com/problems/design-a-number-container-system/

using System.Collections.Generic;

public class NumberContainers {
    private readonly Dictionary<int, int> idx = new();
    private readonly Dictionary<int, SortedSet<int>> heap = new();

    public void Change(int index, int number) {
        idx[index] = number;
        if (!heap.ContainsKey(number)) heap[number] = new SortedSet<int>();
        heap[number].Add(index);
    }

    public int Find(int number) {
        if (!heap.TryGetValue(number, out var h)) return -1;
        while (h.Count > 0) {
            int i = h.Min;
            if (idx[i] == number) return i;
            h.Remove(i);
        }
        return -1;
    }
}
