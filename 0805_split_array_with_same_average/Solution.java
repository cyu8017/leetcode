// LeetCode 0805 - Split Array With Same Average
// https://leetcode.com/problems/split-array-with-same-average/

import java.util.*;

class Solution {
    private int[] nums;
    private int n;
    private Set<Long> memo;

    public boolean splitArraySameAverage(int[] nums) {
        this.nums = nums;
        n = nums.length;
        int total = 0;
        for (int x : nums) total += x;
        Arrays.sort(nums);
        memo = new HashSet<>();
        for (int size = 1; size < n; size++) {
            if ((total * size) % n == 0 && find(total * size / n, size, 0)) return true;
        }
        return false;
    }

    private boolean find(int target, int count, int index) {
        if (count == 0) return target == 0;
        if (index == n || count + index > n || target < 0) return false;
        long key = ((long) target << 20) | ((long) count << 10) | index;
        if (memo.contains(key)) return false;
        if (find(target - nums[index], count - 1, index + 1) || find(target, count, index + 1)) {
            return true;
        }
        memo.add(key);
        return false;
    }
}
