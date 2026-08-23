// LeetCode 0634 - Find the Derangement of An Array
// https://leetcode.com/problems/find-the-derangement-of-an-array/

class Solution {
    public int findDerangement(int n) {
        final int mod = 1000000007;
        if (n == 1) {
            return 0;
        }
        long prev2 = 0;
        long prev1 = 1;
        for (int size = 3; size <= n; ++size) {
            long next = (size - 1) * (prev1 + prev2) % mod;
            prev2 = prev1;
            prev1 = next;
        }
        return (int) prev1;
    }
}
