// LeetCode 2597 - The Number of Beautiful Subsets
// https://leetcode.com/problems/the-number-of-beautiful-subsets/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int beautifulSubsets(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : nums) freq.put(x, freq.getOrDefault(x, 0) + 1);
        Map<Integer, List<Integer>> groups = new HashMap<>();
        for (int key : freq.keySet()) {
            int rem = key % k;
            groups.computeIfAbsent(rem, z -> new ArrayList<>()).add(key);
        }
        int ans = 1;
        for (List<Integer> vals : groups.values()) {
            Collections.sort(vals);
            int prevTake = 0, prevSkip = 1;
            int prevVal = Integer.MIN_VALUE / 2;
            for (int v : vals) {
                int ways = 1;
                for (int i = 0; i < freq.get(v); ++i) ways *= 2;
                ways--;
                int skip = prevTake + prevSkip;
                int take = ways * prevSkip;
                if (prevVal + k != v) take += ways * prevTake;
                prevTake = take;
                prevSkip = skip;
                prevVal = v;
            }
            ans *= prevTake + prevSkip;
        }
        return ans - 1;
    }
}
