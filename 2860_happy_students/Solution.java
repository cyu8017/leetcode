// LeetCode 2860 - Happy Students
// https://leetcode.com/problems/happy-students/

import java.util.Collections;
import java.util.List;

class Solution {
    public int countWays(List<Integer> nums) {
        Collections.sort(nums);
        int n = nums.size(), ans = 0;
        if (nums.get(0) > 0) ans++;
        for (int i = 0; i < n; i++) {
            int selected = i + 1;
            if (selected > nums.get(i) && (i == n - 1 || selected < nums.get(i + 1))) ans++;
        }
        return ans;
    }
}
