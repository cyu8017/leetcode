// LeetCode 2190 - Most Frequent Number Following Key In an Array
// https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

public class Solution {
    public int MostFrequent(int[] nums, int key) {
        var freq = new Dictionary<int, int>();
        int best = 0, ans = 0;
        for (int i = 0; i + 1 < nums.Length; i++) {
            if (nums[i] == key) {
                if (!freq.ContainsKey(nums[i + 1])) freq[nums[i + 1]] = 0;
                freq[nums[i + 1]]++;
                if (freq[nums[i + 1]] > best) {
                    best = freq[nums[i + 1]];
                    ans = nums[i + 1];
                }
            }
        }
        return ans;
    }
}
