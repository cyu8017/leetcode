// LeetCode 0805 - Split Array With Same Average
// https://leetcode.com/problems/split-array-with-same-average/

using System;
using System.Collections.Generic;

public class Solution {
    public bool SplitArraySameAverage(int[] nums) {
        int n = nums.Length, total = 0;
        foreach (int x in nums) total += x;
        Array.Sort(nums);
        var memo = new HashSet<long>();
        bool Find(int target, int count, int index) {
            if (count == 0) return target == 0;
            if (index == n || count + index > n || target < 0) return false;
            long key = ((long)target << 20) | ((long)count << 10) | (uint)index;
            if (memo.Contains(key)) return false;
            if (Find(target - nums[index], count - 1, index + 1) || Find(target, count, index + 1))
                return true;
            memo.Add(key);
            return false;
        }
        for (int size = 1; size < n; size++) {
            if (total * size % n == 0 && Find(total * size / n, size, 0)) return true;
        }
        return false;
    }
}
