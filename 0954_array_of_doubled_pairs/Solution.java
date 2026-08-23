// LeetCode 0954 - Array of Doubled Pairs
// https://leetcode.com/problems/array-of-doubled-pairs/

import java.util.*;

class Solution {
    public boolean canReorderDoubled(int[] arr) {
        TreeMap<Integer, Integer> count = new TreeMap<>();
        for (int x : arr) count.put(x, count.getOrDefault(x, 0) + 1);
        List<Integer> keys = new ArrayList<>(count.keySet());
        keys.sort(Comparator.comparingInt(Math::abs));
        for (int x : keys) {
            int need = count.get(x);
            if (need == 0) continue;
            if (count.getOrDefault(2 * x, 0) < need) return false;
            count.put(2 * x, count.get(2 * x) - need);
        }
        return true;
    }
}
