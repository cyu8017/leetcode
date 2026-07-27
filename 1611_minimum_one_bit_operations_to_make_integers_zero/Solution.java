// LeetCode 1611 - Minimum One Bit Operations to Make Integers Zero
// https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

class Solution {
    public int minimumOneBitOperations(int n) {
        int ans = 0;
        while (n > 0) {
            ans ^= n;
            n >>= 1;
        }
        return ans;
    }
}
