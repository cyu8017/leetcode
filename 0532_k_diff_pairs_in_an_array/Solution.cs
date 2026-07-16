// LeetCode 0532 - K-diff Pairs in an Array
// https://leetcode.com/problems/k-diff-pairs-in-an-array/

public class Solution {
    public int FindPairs(int[] nums, int k) {
        if (k < 0) {
            return 0;
        }

        Dictionary<int, int> freq = new();
        foreach (int num in nums) {
            freq[num] = freq.GetValueOrDefault(num) + 1;
        }

        int pairs = 0;
        foreach (int num in freq.Keys) {
            if (k == 0) {
                if (freq[num] > 1) {
                    pairs++;
                }
            } else if (freq.ContainsKey(num + k)) {
                pairs++;
            }
        }
        return pairs;
    }
}
