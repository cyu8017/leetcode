// LeetCode 1078 - Occurrences After Bigram
// https://leetcode.com/problems/occurrences-after-bigram/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public String[] findOcurrences(String text, String first, String second) {
        String[] words = text.split("\\s+");
        List<String> ans = new ArrayList<>();
        for (int i = 0; i + 2 < words.length; i++) {
            if (words[i].equals(first) && words[i + 1].equals(second)) {
                ans.add(words[i + 2]);
            }
        }
        return ans.toArray(new String[0]);
    }
}
