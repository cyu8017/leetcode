// LeetCode 2964 - Number of Divisible Triplet Sums
// https://leetcode.com/problems/number-of-divisible-triplet-sums/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int divisibleTripletCount(int[] nums, int d) {
        int n = nums.length, ans = 0;
        for (int i = 0; i < n; i++) {
            var freq = new HashMap<Integer, Integer>();
            for (int j = i + 1; j < n; j++) {
                int need = (d - (nums[i] + nums[j]) % d) % d;
                int f = freq.getOrDefault(need, 0);
                ans += f;
                int key = nums[j] % d;
                int f2 = freq.getOrDefault(key, 0);
                freq.put(key, f2 + 1);
            }
        }
        return ans;
    }
}
