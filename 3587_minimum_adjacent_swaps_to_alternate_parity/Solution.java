// LeetCode 3587 - Minimum Adjacent Swaps to Alternate Parity
// https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int minSwaps(int[] nums) {
        List<Integer>[] pos = new ArrayList[2];
        pos[0] = new ArrayList<>();
        pos[1] = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) pos[nums[i] & 1].add(i);
        if (Math.abs(pos[0].size() - pos[1].size()) > 1) return -1;
        if (pos[0].size() > pos[1].size()) return calc(pos, nums.length, 0);
        if (pos[0].size() < pos[1].size()) return calc(pos, nums.length, 1);
        return Math.min(calc(pos, nums.length, 0), calc(pos, nums.length, 1));
    }

    int calc(List<Integer>[] pos, int n, int k) {
        int res = 0;
        for (int i = 0; i < n; i += 2) res += Math.abs(pos[k].get(i / 2) - i);
        return res;
    }
}
