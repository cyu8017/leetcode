// LeetCode 3412 - Find Mirror Score of a String
// https://leetcode.com/problems/find-mirror-score-of-a-string/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public long calculateScore(String s) {
        @SuppressWarnings("unchecked")
        List<Integer>[] stacks = new ArrayList[26];
        for (int i = 0; i < 26; i++) stacks[i] = new ArrayList<>();
        long ans = 0;
        for (int i = 0; i < s.length(); i++) {
            int ci = s.charAt(i) - 'a';
            int mir = 25 - ci;
            if (!stacks[mir].isEmpty()) {
                int j = stacks[mir].remove(stacks[mir].size() - 1);
                ans += i - j;
            } else {
                stacks[ci].add(i);
            }
        }
        return ans;
    }
}
