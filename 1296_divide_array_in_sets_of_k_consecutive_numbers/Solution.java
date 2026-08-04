// LeetCode 1296 - Divide Array in Sets of K Consecutive Numbers
// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

import java.util.*;

class Solution {
    public boolean isPossibleDivide(int[] nums, int k) {
        if (nums.length % k != 0) return false;
        TreeMap<Integer, Integer> counts = new TreeMap<>();
        for (int x : nums) counts.put(x, counts.getOrDefault(x, 0) + 1);
        while (!counts.isEmpty()) {
            int start = counts.firstKey();
            int amount = counts.get(start);
            if (amount == 0) {
                counts.remove(start);
                continue;
            }
            for (int value = start; value < start + k; value++) {
                if (!counts.containsKey(value) || counts.get(value) < amount) return false;
                counts.put(value, counts.get(value) - amount);
                if (counts.get(value) == 0) counts.remove(value);
            }
        }
        return true;
    }
}
