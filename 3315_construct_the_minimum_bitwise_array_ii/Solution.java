// LeetCode 3315 - Construct the Minimum Bitwise Array II
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] minBitwiseArray(List<Integer> nums) {
        int[] ans = new int[nums.size()];
        Arrays.fill(ans, -1);
        for (int i = 0; i < nums.size(); i++) {
            int n = nums.get(i);
            if (n == 2) continue;
            for (int b = 0; b < 31; b++) {
                if (((n >> b) & 1) == 0) continue;
                int x = n ^ (1 << b);
                if ((x | (x + 1)) == n) { ans[i] = x; break; }
            }
        }
        return ans;
    }
}
