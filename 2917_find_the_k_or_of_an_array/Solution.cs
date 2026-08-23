// LeetCode 2917 - Find the K-or of an Array
// https://leetcode.com/problems/find-the-k-or-of-an-array/

public class Solution {
    public int FindKOr(int[] nums, int k) {
        int ans = 0;
        for (int b = 0; b < 31; b++) {
            int cnt = 0;
            foreach (int v in nums) if ((v & (1 << b)) != 0) cnt++;
            if (cnt >= k) ans |= 1 << b;
        }
        return ans;
    }
}
