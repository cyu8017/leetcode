// LeetCode 0300 - Longest Increasing Subsequence
// https://leetcode.com/problems/longest-increasing-subsequence/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> piles = new ArrayList<>();
        for (int num : nums) {
            int left = 0;
            int right = piles.size();
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (piles.get(mid) < num) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            if (left == piles.size()) {
                piles.add(num);
            } else {
                piles.set(left, num);
            }
        }
        return piles.size();
    }
}
