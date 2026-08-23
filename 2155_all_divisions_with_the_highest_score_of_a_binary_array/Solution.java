// LeetCode 2155 - All Divisions With the Highest Score of a Binary Array
// https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

import java.util.*;

class Solution {
    public List<Integer> maxScoreIndices(int[] nums) {
        int n = nums.length;
        int total1 = 0;
        for (int x : nums) total1 += x;
        int best = total1, left0 = 0, right1 = total1;
        List<Integer> ans = new ArrayList<>();
        ans.add(0);
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) left0++;
            else right1--;
            int score = left0 + right1;
            if (score > best) { best = score; ans = new ArrayList<>(); ans.add(i + 1); }
            else if (score == best) ans.add(i + 1);
        }
        return ans;
    }
}
