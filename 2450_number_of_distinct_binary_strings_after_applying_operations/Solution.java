// LeetCode 2450 - Number of Distinct Binary Strings After Applying Operations
// https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/

class Solution {
    public int countDistinctStrings(String s, int k) {
        final int mod = 1000000007;
        int n = s.length();
        int ans = 1;
        for (int i = 0; i < n - k + 1; i++)
            ans = (int)(ans * 2L % mod);
        return ans;
    }
}
