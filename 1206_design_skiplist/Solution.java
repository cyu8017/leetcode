// LeetCode 1206 - Design Skiplist
// https://leetcode.com/problems/design-skiplist/

import java.util.*;

class Skiplist {
    private final List<Integer> values = new ArrayList<>();

    public Skiplist() {}

    public boolean search(int target) {
        int i = Collections.binarySearch(values, target);
        return i >= 0;
    }

    public void add(int num) {
        int i = Collections.binarySearch(values, num);
        if (i < 0) i = -i - 1;
        values.add(i, num);
    }

    public boolean erase(int num) {
        int i = Collections.binarySearch(values, num);
        if (i < 0) return false;
        values.remove(i);
        return true;
    }
}
