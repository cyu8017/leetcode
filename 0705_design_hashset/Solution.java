// LeetCode 0705 - Design HashSet
// https://leetcode.com/problems/design-hashset/

import java.util.*;

class MyHashSet {
    private final Set<Integer> data = new HashSet<>();

    public MyHashSet() {}

    public void add(int key) { data.add(key); }

    public void remove(int key) { data.remove(key); }

    public boolean contains(int key) { return data.contains(key); }
}
