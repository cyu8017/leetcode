// LeetCode 0146 - LRU Cache
// https://leetcode.com/problems/lru-cache/

using System.Collections.Generic;
public class LRUCache {
    private class Node { public int key, value; public Node prev, next; public Node(int key, int value) { this.key = key; this.value = value; } }
    private readonly int capacity;
    private readonly Dictionary<int, Node> cache = new Dictionary<int, Node>();
    private readonly Node head = new Node(0, 0), tail = new Node(0, 0);
    public LRUCache(int capacity) { this.capacity = capacity; head.next = tail; tail.prev = head; }
    public int Get(int key) { if (!cache.TryGetValue(key, out var node)) return -1; MoveToFront(node); return node.value; }
    public void Put(int key, int value) {
        if (cache.TryGetValue(key, out var node)) { node.value = value; MoveToFront(node); return; }
        if (cache.Count == capacity) { var lru = tail.prev; Remove(lru); cache.Remove(lru.key); }
        node = new Node(key, value); cache[key] = node; AddFront(node);
    }
    private void MoveToFront(Node node) { Remove(node); AddFront(node); }
    private void Remove(Node node) { node.prev.next = node.next; node.next.prev = node.prev; }
    private void AddFront(Node node) { node.prev = head; node.next = head.next; head.next.prev = node; head.next = node; }
}