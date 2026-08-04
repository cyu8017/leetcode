// LeetCode 1354 - Construct Target Array With Multiple Sums
// https://leetcode.com/problems/construct-target-array-with-multiple-sums/

import java.util.*;

class Solution {
    public boolean isPossible(int[] target) {
        if (target.length == 1) return target[0] == 1;
        PriorityQueue<Long> h = new PriorityQueue<>(Collections.reverseOrder());
        long total = 0;
        for (int x : target) {
            h.offer((long) x);
            total += x;
        }
        while (true) {
            long x = h.poll();
            long rest = total - x;
            if (x == 1 || rest == 1) return true;
            if (rest == 0 || x <= rest) return false;
            long prev = x % rest;
            if (prev == 0) return false;
            total = rest + prev;
            h.offer(prev);
        }
    }
}
