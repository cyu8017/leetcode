// LeetCode 3314 - Construct the Minimum Bitwise Array I
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] minBitwiseArray(List<Integer> nums) {
        int[] ans = new int[nums.size()];
        Arrays.fill(ans, -1);
        for (int i = 0; i < nums.size(); i++) {
            int n = nums.get(i);
            for (int x = 0; x < n; x++) {
                if ((x | (x + 1)) == n) { ans[i] = x; break; }
            }
        }
        return ans;
    }
}
