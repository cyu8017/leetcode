// LeetCode 2450 - Number of Distinct Binary Strings After Applying Operations
// https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/

public class Solution {
    public int CountDistinctStrings(string s, int k) {
        const int mod = 1000000007;
        int n = s.Length;
        int ans = 1;
        for (int i = 0; i < n - k + 1; i++)
            ans = (int)(ans * 2L % mod);
        return ans;
    }
}
