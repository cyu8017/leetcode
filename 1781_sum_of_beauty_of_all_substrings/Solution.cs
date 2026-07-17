// LeetCode 1781 - Sum of Beauty of All Substrings
// https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

public class Solution {
    public int BeautySum(string s) {
        int ans = 0;
        for (int i = 0; i < s.Length; i++) {
            int[] freq = new int[26];
            for (int j = i; j < s.Length; j++) {
                freq[s[j] - 'a']++;
                int lo = int.MaxValue;
                int hi = 0;
                foreach (int count in freq) {
                    if (count > 0) {
                        lo = Math.Min(lo, count);
                        hi = Math.Max(hi, count);
                    }
                }
                ans += hi - lo;
            }
        }
        return ans;
    }
}
