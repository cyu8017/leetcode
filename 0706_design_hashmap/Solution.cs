// LeetCode 0706 - Design HashMap
// https://leetcode.com/problems/design-hashmap/

using System.Collections.Generic;

public class MyHashMap {
    private readonly Dictionary<int, int> data = new Dictionary<int, int>();
    public MyHashMap() { }
    public void Put(int key, int value) => data[key] = value;
    public int Get(int key) => data.TryGetValue(key, out int v) ? v : -1;
    public void Remove(int key) => data.Remove(key);
}
