// LeetCode 1852 - Distinct Numbers in Each Subarray
// https://leetcode.com/problems/distinct-numbers-in-each-subarray/

public class Solution {
    public int[] DistinctNumbers(int[] nums, int k) {
        var counts = new Dictionary<int, int>();
        for (int i = 0; i < k; i++) {
            counts[nums[i]] = counts.GetValueOrDefault(nums[i]) + 1;
        }
        var result = new List<int> { counts.Count };
        int left = 0;
        for (int right = k; right < nums.Length; right++) {
            counts[nums[right]] = counts.GetValueOrDefault(nums[right]) + 1;
            int outgoing = nums[left];
            counts[outgoing]--;
            if (counts[outgoing] == 0) {
                counts.Remove(outgoing);
            }
            left++;
            result.Add(counts.Count);
        }
        return result.ToArray();
    }
}
