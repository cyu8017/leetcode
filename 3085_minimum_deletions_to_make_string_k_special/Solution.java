// LeetCode 3085 - Minimum Deletions to Make String K-Special
// https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int minimumDeletions(String word, int k) {
        int[] freq = new int[26];
        for (int i = 0; i < word.length(); i++) freq[word.charAt(i) - 'a']++;
        List<Integer> nums = new ArrayList<>();
        for (int v : freq) if (v > 0) nums.add(v);
        int ans = word.length();
        for (int i = 0; i <= word.length(); i++) {
            int cur = 0;
            for (int x : nums) {
                if (x < i) cur += x;
                else if (x > i + k) cur += x - i - k;
            }
            ans = Math.min(ans, cur);
        }
        return ans;
    }
}
