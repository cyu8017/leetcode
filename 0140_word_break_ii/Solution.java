// LeetCode 0140 - Word Break II
// https://leetcode.com/problems/word-break-ii/

import java.util.*;

class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        return sentences(s, 0, new HashSet<>(wordDict), new HashMap<>());
    }

    private List<String> sentences(String s, int start, Set<String> words, Map<Integer, List<String>> memo) {
        if (memo.containsKey(start)) return memo.get(start);
        List<String> result = new ArrayList<>();
        if (start == s.length()) {
            result.add("");
        } else {
            for (int end = start + 1; end <= s.length(); end++) {
                String word = s.substring(start, end);
                if (!words.contains(word)) continue;
                for (String tail : sentences(s, end, words, memo)) result.add(tail.isEmpty() ? word : word + " " + tail);
            }
        }
        memo.put(start, result);
        return result;
    }
}
