// LeetCode 1403 - Minimum Subsequence In Non Increasing Order
// https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

using System;
using System.Collections.Generic;
using System.Linq;
public class Solution {
    public IList<int> MinSubsequence(int[] nums) {
        var answer = new List<int>(); int chosen = 0, total = nums.Sum();
        foreach (int value in nums.OrderByDescending(x => x)) {
            answer.Add(value); chosen += value;
            if (chosen > total - chosen) return answer;
        }
        return answer;
    }
}
