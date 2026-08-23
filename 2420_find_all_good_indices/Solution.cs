// LeetCode 2420 - Find All Good Indices
// https://leetcode.com/problems/find-all-good-indices/

using System.Collections.Generic;

public class Solution {
    public IList<int> GoodIndices(int[] nums, int k) {
        int n = nums.Length;
        int[] dec = new int[n], inc = new int[n];
        dec[0] = 1;
        for (int i = 1; i < n; i++)
            dec[i] = nums[i] <= nums[i - 1] ? dec[i - 1] + 1 : 1;
        inc[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--)
            inc[i] = nums[i] <= nums[i + 1] ? inc[i + 1] + 1 : 1;
        var ans = new List<int>();
        for (int i = k; i < n - k; i++) {
            if (dec[i - 1] >= k && inc[i + 1] >= k) ans.Add(i);
        }
        return ans;
    }
}
