// LeetCode 0146 - LRU Cache
// https://leetcode.com/problems/lru-cache/

import java.util.*;
class LRUCache {
    private class Node { int key, value; Node prev, next; Node(int key, int value) { this.key = key; this.value = value; } }
    private final int capacity;
    private final Map<Integer, Node> cache = new HashMap<>();
    private final Node head = new Node(0, 0), tail = new Node(0, 0);
    public LRUCache(int capacity) { this.capacity = capacity; head.next = tail; tail.prev = head; }
    public int get(int key) { Node node = cache.get(key); if (node == null) return -1; moveToFront(node); return node.value; }
    public void put(int key, int value) {
        Node node = cache.get(key);
        if (node != null) { node.value = value; moveToFront(node); return; }
        if (cache.size() == capacity) { Node lru = tail.prev; remove(lru); cache.remove(lru.key); }
        node = new Node(key, value); cache.put(key, node); addFront(node);
    }
    private void moveToFront(Node node) { remove(node); addFront(node); }
    private void remove(Node node) { node.prev.next = node.next; node.next.prev = node.prev; }
    private void addFront(Node node) { node.prev = head; node.next = head.next; head.next.prev = node; head.next = node; }
}