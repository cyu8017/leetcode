// LeetCode 1486 - Xor Operation In An Array
// https://leetcode.com/problems/xor-operation-in-an-array/

public class Solution {
    public int XorOperation(int n, int start) {
        int ans = 0;
        for (int i = 0; i < n; i++) ans ^= start + 2 * i;
        return ans;
    }
}
