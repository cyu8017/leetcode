// LeetCode 0446 - Arithmetic Slices II - Subsequence
// https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

using System.Collections.Generic;

public class Solution {
    public int NumberOfArithmeticSlices(int[] nums) {
        int total = 0;
        Dictionary<long, int>[] differences = new Dictionary<long, int>[nums.Length];
        for (int index = 0; index < nums.Length; index++) {
            differences[index] = new Dictionary<long, int>();
        }

        for (int index = 0; index < nums.Length; index++) {
            for (int previous = 0; previous < index; previous++) {
                long diff = (long)nums[index] - nums[previous];
                total += differences[previous].GetValueOrDefault(diff, 0);
                if (!differences[index].ContainsKey(diff)) {
                    differences[index][diff] = 0;
                }
                differences[index][diff] +=
                    differences[previous].GetValueOrDefault(diff, 0) + 1;
            }
        }

        return total;
    }
}
