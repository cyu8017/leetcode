// LeetCode 2336 - Smallest Number in Infinite Set
// https://leetcode.com/problems/smallest-number-in-infinite-set/

using System.Collections.Generic;

public class SmallestInfiniteSet {
    private int next = 1;
    private readonly HashSet<int> added = new();
    private readonly SortedSet<int> heap = new();

    public int PopSmallest() {
        if (heap.Count > 0) {
            int x = heap.Min;
            heap.Remove(x);
            added.Remove(x);
            return x;
        }
        return next++;
    }

    public void AddBack(int num) {
        if (num < next && !added.Contains(num)) {
            added.Add(num);
            heap.Add(num);
        }
    }
}
