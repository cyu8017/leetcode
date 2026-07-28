// LeetCode 1002 - Find Common Characters
// https://leetcode.com/problems/find-common-characters/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<String> commonChars(String[] words) {
        int[] common = new int[26];
        Arrays.fill(common, Integer.MAX_VALUE);
        for (String w : words) {
            int[] cnt = new int[26];
            for (char ch : w.toCharArray()) cnt[ch - 'a']++;
            for (int i = 0; i < 26; i++) common[i] = Math.min(common[i], cnt[i]);
        }
        List<String> ans = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            while (common[i]-- > 0) ans.add(String.valueOf((char) ('a' + i)));
        }
        return ans;
    }
}
