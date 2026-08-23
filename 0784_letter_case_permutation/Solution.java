// LeetCode 0784 - Letter Case Permutation
// https://leetcode.com/problems/letter-case-permutation/

import java.util.*;

class Solution {
    public List<String> letterCasePermutation(String s) {
        List<String> result = new ArrayList<>();
        result.add("");
        for (char ch : s.toCharArray()) {
            List<String> next = new ArrayList<>();
            if (Character.isLetter(ch)) {
                char lower = Character.toLowerCase(ch);
                char upper = Character.toUpperCase(ch);
                for (String prefix : result) {
                    next.add(prefix + lower);
                    next.add(prefix + upper);
                }
            } else {
                for (String prefix : result) next.add(prefix + ch);
            }
            result = next;
        }
        return result;
    }
}
