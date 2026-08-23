// LeetCode 0705 - Design HashSet
// https://leetcode.com/problems/design-hashset/

using System.Collections.Generic;

public class MyHashSet {
    private readonly HashSet<int> data = new HashSet<int>();
    public MyHashSet() { }
    public void Add(int key) => data.Add(key);
    public void Remove(int key) => data.Remove(key);
    public bool Contains(int key) => data.Contains(key);
}
