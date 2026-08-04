// LeetCode 1999 - Smallest Greater Multiple Made of Two Digits
// https://leetcode.com/problems/smallest-greater-multiple-made-of-two-digits/

import java.util.*;

class Solution {
    public int findInteger(int k, int digit1, int digit2) {
        TreeSet<Integer> digits = new TreeSet<>();
        digits.add(digit1);
        digits.add(digit2);
        Queue<Long> q = new ArrayDeque<>();
        Set<Long> seen = new HashSet<>();
        for (int d : digits) {
            if (d != 0) {
                q.offer((long) d);
                seen.add((long) d);
            }
        }
        if (q.isEmpty()) return -1;
        long limit = Integer.MAX_VALUE;
        while (!q.isEmpty()) {
            long x = q.poll();
            if (x > k && x % k == 0) return (int) x;
            for (int d : digits) {
                long nx = x * 10 + d;
                if (nx <= limit && seen.add(nx)) q.offer(nx);
            }
        }
        return -1;
    }
}
