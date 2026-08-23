// LeetCode 0846 - Hand of Straights
// https://leetcode.com/problems/hand-of-straights/

import java.util.*;

class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        if (hand.length % groupSize != 0) return false;
        TreeMap<Integer, Integer> count = new TreeMap<>();
        for (int x : hand) count.merge(x, 1, Integer::sum);
        while (!count.isEmpty()) {
            int start = count.firstKey();
            for (int x = start; x < start + groupSize; x++) {
                Integer c = count.get(x);
                if (c == null) return false;
                if (c == 1) count.remove(x);
                else count.put(x, c - 1);
            }
        }
        return true;
    }
}
