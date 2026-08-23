// LeetCode 2349 - Design a Number Container System
// https://leetcode.com/problems/design-a-number-container-system/

import java.util.HashMap;
import java.util.Map;
import java.util.TreeSet;

class NumberContainers {
    private final Map<Integer, Integer> idx = new HashMap<>();
    private final Map<Integer, TreeSet<Integer>> heap = new HashMap<>();

    public void change(int index, int number) {
        idx.put(index, number);
        heap.computeIfAbsent(number, k -> new TreeSet<>()).add(index);
    }

    public int find(int number) {
        TreeSet<Integer> h = heap.get(number);
        if (h == null) return -1;
        while (!h.isEmpty()) {
            int i = h.first();
            if (idx.get(i) != null && idx.get(i) == number) return i;
            h.pollFirst();
        }
        return -1;
    }
}
