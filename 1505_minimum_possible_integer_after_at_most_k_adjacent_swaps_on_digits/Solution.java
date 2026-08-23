// LeetCode 1505 - Minimum Possible Integer After at Most K Adjacent Swaps On Digits
// https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/

import java.util.*;

class Solution {
    public String minInteger(String num, int k) {
        Deque<Integer>[] positions = new Deque[10];
        for (int i = 0; i < 10; i++) {
            positions[i] = new ArrayDeque<>();
        }
        for (int i = 0; i < num.length(); i++) {
            positions[num.charAt(i) - '0'].addLast(i);
        }

        FenwickTree fw = new FenwickTree(num.length());
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < num.length(); i++) {
            for (int digit = 0; digit < 10; digit++) {
                if (positions[digit].isEmpty()) {
                    continue;
                }
                int index = positions[digit].peekFirst();
                int cost = index - fw.sum(index);
                if (cost <= k) {
                    k -= cost;
                    positions[digit].pollFirst();
                    fw.add(index, 1);
                    out.append((char) ('0' + digit));
                    break;
                }
            }
        }
        return out.toString();
    }

    private static class FenwickTree {
        private final int[] bit;

        FenwickTree(int n) {
            bit = new int[n + 1];
        }

        void add(int i, int delta) {
            for (i++; i < bit.length; i += i & -i) {
                bit[i] += delta;
            }
        }

        int sum(int i) {
            int out = 0;
            while (i > 0) {
                out += bit[i];
                i -= i & -i;
            }
            return out;
        }
    }
}
