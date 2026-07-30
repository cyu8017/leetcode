// LeetCode 1206 - Design Skiplist
// https://leetcode.com/problems/design-skiplist/

using System.Collections.Generic;

public class Skiplist {
    private readonly List<int> values = new List<int>();

    public bool Search(int target) {
        int i = values.BinarySearch(target);
        return i >= 0;
    }

    public void Add(int num) {
        int i = values.BinarySearch(num);
        if (i < 0) i = ~i;
        values.Insert(i, num);
    }

    public bool Erase(int num) {
        int i = values.BinarySearch(num);
        if (i < 0) return false;
        values.RemoveAt(i);
        return true;
    }
}
