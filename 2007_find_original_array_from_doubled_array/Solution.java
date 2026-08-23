// LeetCode 2007 - Find Original Array From Doubled Array
// https://leetcode.com/problems/find-original-array-from-doubled-array/

import java.util.*;

class Solution {
    public int[] findOriginalArray(int[] changed) {
        if (changed.length % 2 != 0) return new int[0];
        Arrays.sort(changed);
        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : changed) freq.merge(x, 1, Integer::sum);
        List<Integer> ans = new ArrayList<>();
        for (int x : changed) {
            if (freq.getOrDefault(x, 0) == 0) continue;
            freq.put(x, freq.get(x) - 1);
            if (freq.getOrDefault(2 * x, 0) == 0) return new int[0];
            freq.put(2 * x, freq.get(2 * x) - 1);
            ans.add(x);
        }
        return ans.stream().mapToInt(i -> i).toArray();
    }
}
