// LeetCode 1825 - Finding MK Average
// https://leetcode.com/problems/finding-mk-average/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.List;

class MKAverage {
    private final int m;
    private final int k;
    private final Deque<Integer> stream = new ArrayDeque<>();

    public MKAverage(int m, int k) {
        this.m = m;
        this.k = k;
    }

    public void addElement(int num) {
        stream.addLast(num);
    }

    public int calculateMKAverage() {
        if (stream.size() < m) {
            return -1;
        }
        List<Integer> window = new ArrayList<>();
        int skip = stream.size() - m;
        int index = 0;
        for (int num : stream) {
            if (index++ >= skip) {
                window.add(num);
            }
        }
        Collections.sort(window);
        int sum = 0;
        for (int i = k; i < window.size() - k; i++) {
            sum += window.get(i);
        }
        return sum / (window.size() - 2 * k);
    }
}
