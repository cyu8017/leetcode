// LeetCode 1781 - Sum of Beauty of All Substrings
// https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

class Solution {
    public int beautySum(String s) {
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            int[] freq = new int[26];
            for (int j = i; j < s.length(); j++) {
                freq[s.charAt(j) - 'a']++;
                int lo = Integer.MAX_VALUE;
                int hi = 0;
                for (int count : freq) {
                    if (count > 0) {
                        lo = Math.min(lo, count);
                        hi = Math.max(hi, count);
                    }
                }
                ans += hi - lo;
            }
        }
        return ans;
    }
}
