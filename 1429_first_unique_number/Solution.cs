// LeetCode 1429 - First Unique Number
// https://leetcode.com/problems/first-unique-number/

using System.Collections.Generic;
public class FirstUnique {
    Dictionary<int, int> counts = new Dictionary<int, int>();
    LinkedList<int> unique = new LinkedList<int>();
    Dictionary<int, LinkedListNode<int>> nodes = new Dictionary<int, LinkedListNode<int>>();
    public FirstUnique(int[] nums) { foreach (int v in nums) Add(v); }
    public int ShowFirstUnique() => unique.Count == 0 ? -1 : unique.First.Value;
    public void Add(int value) {
        if (!counts.ContainsKey(value)) counts[value] = 0;
        counts[value]++;
        if (counts[value] == 1) nodes[value] = unique.AddLast(value);
        else if (nodes.ContainsKey(value)) { unique.Remove(nodes[value]); nodes.Remove(value); }
    }
}
