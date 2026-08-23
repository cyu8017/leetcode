// LeetCode 0706 - Design HashMap
// https://leetcode.com/problems/design-hashmap/

import java.util.*;

class MyHashMap {
    private final Map<Integer, Integer> data = new HashMap<>();

    public MyHashMap() {}

    public void put(int key, int value) { data.put(key, value); }

    public int get(int key) { return data.getOrDefault(key, -1); }

    public void remove(int key) { data.remove(key); }
}
