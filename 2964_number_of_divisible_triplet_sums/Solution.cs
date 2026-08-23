// LeetCode 2964 - Number of Divisible Triplet Sums
// https://leetcode.com/problems/number-of-divisible-triplet-sums/

using System.Collections.Generic;

public class Solution {
    public int DivisibleTripletCount(int[] nums, int d) {
        int n = nums.Length, ans = 0;
        for (int i = 0; i < n; i++) {
            var freq = new Dictionary<int, int>();
            for (int j = i + 1; j < n; j++) {
                int need = (d - (nums[i] + nums[j]) % d) % d;
                freq.TryGetValue(need, out int f);
                ans += f;
                int key = nums[j] % d;
                freq.TryGetValue(key, out int f2);
                freq[key] = f2 + 1;
            }
        }
        return ans;
    }
}
