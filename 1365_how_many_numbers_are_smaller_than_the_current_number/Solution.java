// LeetCode 1365 - How Many Numbers Are Smaller Than The Current Number
// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

import java.util.*;

class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        var sorted = (int[])nums.Clone();
        Arrays.sort(sorted);
        var answer = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            int lo = 0, hi = sorted.length;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (sorted[mid] < nums[i]) lo = mid + 1; else hi = mid;
            }
            answer[i] = lo;
        }
        return answer;
    }
}
