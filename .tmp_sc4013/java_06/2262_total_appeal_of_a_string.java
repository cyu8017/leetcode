// LeetCode 2262 - Total Appeal of A String
// https://leetcode.com/problems/total-appeal-of-a-string/

import java.util.Arrays;

class Solution {
    public long appealSum(String s) {
        int[] last = new int[26];
        Arrays.fill(last, -1);
        long ans = 0, cur = 0;
        for (int i = 0; i < s.length(); i++) {
            int c = s.charAt(i) - 'a';
            cur += i - last[c];
            last[c] = i;
            ans += cur;
        }
        return ans;
    }
}
