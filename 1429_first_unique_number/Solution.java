// LeetCode 1429 - First Unique Number
// https://leetcode.com/problems/first-unique-number/

import java.util.*;

class FirstUnique {
    private Map<Integer, Integer> freq = new HashMap<>();
    private Queue<Integer> queue = new ArrayDeque<>();

    public FirstUnique(int[] nums) {
        for (int x : nums) add(x);
    }

    public int showFirstUnique() {
        while (!queue.isEmpty() && freq.get(queue.peek()) > 1) queue.poll();
        return queue.isEmpty() ? -1 : queue.peek();
    }

    public void add(int value) {
        freq.merge(value, 1, Integer::sum);
        if (freq.get(value) == 1) queue.offer(value);
    }
}
