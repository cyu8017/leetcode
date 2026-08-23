// LeetCode 2942 - Find Words Containing Character
// https://leetcode.com/problems/find-words-containing-character/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            if (words[i].indexOf(x) >= 0) ans.add(i);
        }
        return ans;
    }
}
