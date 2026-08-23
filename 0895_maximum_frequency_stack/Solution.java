// LeetCode 0895 - Maximum Frequency Stack
// https://leetcode.com/problems/maximum-frequency-stack/

import java.util.*;

class FreqStack {
    private Map<Integer, Integer> freq = new HashMap<>();
    private Map<Integer, List<Integer>> group = new HashMap<>();
    private int maxfreq;

    public FreqStack() {
        maxfreq = 0;
    }

    public void push(int val) {
        int f = freq.getOrDefault(val, 0) + 1;
        freq.put(val, f);
        maxfreq = Math.max(maxfreq, f);
        group.computeIfAbsent(f, k -> new ArrayList<>()).add(val);
    }

    public int pop() {
        List<Integer> list = group.get(maxfreq);
        int val = list.remove(list.size() - 1);
        freq.put(val, freq.get(val) - 1);
        if (list.isEmpty()) maxfreq--;
        return val;
    }
}
