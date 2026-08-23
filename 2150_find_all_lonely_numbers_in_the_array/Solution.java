// LeetCode 2150 - Find All Lonely Numbers in the Array
// https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

import java.util.*;

class Solution {
    public List<Integer> findLonely(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : nums) freq.merge(x, 1, Integer::sum);
        List<Integer> ans = new ArrayList<>();
        for (Map.Entry<Integer, Integer> kv : freq.entrySet())
            if (kv.getValue() == 1 && !freq.containsKey(kv.getKey() - 1) && !freq.containsKey(kv.getKey() + 1))
                ans.add(kv.getKey());
        return ans;
    }
}
