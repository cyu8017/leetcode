// LeetCode 1636 - Sort Array by Increasing Frequency
// https://leetcode.com/problems/sort-array-by-increasing-frequency/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] FrequencySort(int[] nums) {
        var count = new Dictionary<int, int>();
        foreach (int x in nums) count[x] = count.GetValueOrDefault(x) + 1;
        return nums.OrderBy(x => count[x]).ThenByDescending(x => x).ToArray();
    }
}
