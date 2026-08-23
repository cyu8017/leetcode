// LeetCode 2788 - Split Strings by Separator
// https://leetcode.com/problems/split-strings-by-separator/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> splitWordsBySeparator(List<String> words, char separator) {
        List<String> ans = new ArrayList<>();
        for (String w : words) {
            int start = 0;
            for (int i = 0; i <= w.length(); i++) {
                if (i == w.length() || w.charAt(i) == separator) {
                    if (i > start) ans.add(w.substring(start, i));
                    start = i + 1;
                }
            }
        }
        return ans;
    }
}
