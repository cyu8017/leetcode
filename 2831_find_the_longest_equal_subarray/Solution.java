// LeetCode 2831 - Find the Longest Equal Subarray
// https://leetcode.com/problems/find-the-longest-equal-subarray/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int longestEqualSubarray(List<Integer> nums, int k) {
        var pos = new HashMap<Integer, List<Integer>>();
        for (int i = 0; i < nums.size(); i++) {
            if (!pos.containsKey(nums.get(i))) pos.put(nums.get(i), new ArrayList<Integer>());
            pos.get(nums.get(i)).add(i);
        }
        int ans = 0;
        for (var p : pos.values()) {
            int left = 0;
            for (int right = 0; right < p.size(); right++) {
                while (p[right] - p[left] - (right - left) > k) left++;
                ans = Math.max(ans, right - left + 1);
            }
        }
        return ans;
    }
}
