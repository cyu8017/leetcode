// LeetCode 2248 - Intersection of Multiple Arrays
// https://leetcode.com/problems/intersection-of-multiple-arrays/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    public List<Integer> intersection(int[][] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int[] arr : nums) {
            Set<Integer> seen = new HashSet<>();
            for (int x : arr) {
                if (seen.add(x)) freq.put(x, freq.getOrDefault(x, 0) + 1);
            }
        }
        List<Integer> ans = new ArrayList<>();
        for (Map.Entry<Integer, Integer> kv : freq.entrySet())
            if (kv.getValue() == nums.length) ans.add(kv.getKey());
        Collections.sort(ans);
        return ans;
    }
}
