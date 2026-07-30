// LeetCode 1313 - Decompress Run Length Encoded List
// https://leetcode.com/problems/decompress-run-length-encoded-list/

using System.Collections.Generic;

public class Solution {
    public int[] DecompressRLElist(int[] nums) {
        var answer = new List<int>();
        for (int i = 0; i < nums.Length; i += 2)
            for (int j = 0; j < nums[i]; j++)
                answer.Add(nums[i + 1]);
        return answer.ToArray();
    }
}
