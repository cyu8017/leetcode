// LeetCode 3785 - Minimum Swaps to Avoid Forbidden Values
// https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minSwaps(int[] nums, int[] forbidden) {
        int n = nums.length;
        var freq = new HashMap<Integer, Integer>();
        for (int x : nums) {
            if (!freq.containsKey(x)) freq.put(x, 0);
            freq.merge(x, 1, Integer::sum);
        }
        for (int x : forbidden) {
            if (!freq.containsKey(x)) freq.put(x, 0);
            freq.merge(x, 1, Integer::sum);
        }
        for (var c : freq.values()) {
            if (c > n) return -1;
        }
        var bad = new HashMap<Integer, Integer>();
        int total = 0, largest = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == forbidden[i]) {
                if (!bad.containsKey(nums[i])) bad.put(nums[i], 0);
                bad.merge(nums[i], 1, Integer::sum);
                total++;
                if (bad.get(nums[i]) > largest) largest = bad.get(nums[i]);
            }
        }
        if ((total + 1) / 2 > largest) return (total + 1) / 2;
        return largest;
    }
}
