// LeetCode 0820 - Short Encoding of Words
// https://leetcode.com/problems/short-encoding-of-words/

import java.util.*;

class Solution {
    public int minimumLengthEncoding(String[] words) {
        Set<String> good = new HashSet<>(Arrays.asList(words));
        for (String word : words) {
            for (int i = 1; i < word.length(); i++) good.remove(word.substring(i));
        }
        int ans = 0;
        for (String word : good) ans += word.length() + 1;
        return ans;
    }
}
