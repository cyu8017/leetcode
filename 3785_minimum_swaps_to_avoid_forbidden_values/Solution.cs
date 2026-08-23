// LeetCode 3785 - Minimum Swaps to Avoid Forbidden Values
// https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/

using System.Collections.Generic;

public class Solution {
    public int MinSwaps(int[] nums, int[] forbidden) {
        int n = nums.Length;
        var freq = new Dictionary<int, int>();
        foreach (int x in nums) {
            if (!freq.ContainsKey(x)) freq[x] = 0;
            freq[x]++;
        }
        foreach (int x in forbidden) {
            if (!freq.ContainsKey(x)) freq[x] = 0;
            freq[x]++;
        }
        foreach (var c in freq.Values) {
            if (c > n) return -1;
        }
        var bad = new Dictionary<int, int>();
        int total = 0, largest = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == forbidden[i]) {
                if (!bad.ContainsKey(nums[i])) bad[nums[i]] = 0;
                bad[nums[i]]++;
                total++;
                if (bad[nums[i]] > largest) largest = bad[nums[i]];
            }
        }
        if ((total + 1) / 2 > largest) return (total + 1) / 2;
        return largest;
    }
}
