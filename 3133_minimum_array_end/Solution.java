// LeetCode 3133 - Minimum Array End
// https://leetcode.com/problems/minimum-array-end/

class Solution {
    public long minEnd(int n, int x) {
        n--;
        long ans = x;
        for (int i = 0; i < 31; i++) {
            if (((x >> i) & 1) == 0) {
                ans |= (long)(n & 1) << i;
                n >>= 1;
            }
        }
        ans |= (long)n << 31;
        return ans;
    }
}
