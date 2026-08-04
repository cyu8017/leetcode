// LeetCode 1324 - Print Words Vertically
// https://leetcode.com/problems/print-words-vertically/

import java.util.*;

class Solution {
    public List<String> printVertically(String s) {
        String[] words = s.split(" ");
        int max = 0;
        for (String w : words) max = Math.max(max, w.length());
        List<String> answer = new ArrayList<>();
        for (int i = 0; i < max; i++) {
            StringBuilder sb = new StringBuilder();
            for (String word : words) {
                sb.append(i < word.length() ? word.charAt(i) : ' ');
            }
            while (sb.length() > 0 && sb.charAt(sb.length() - 1) == ' ') sb.setLength(sb.length() - 1);
            answer.add(sb.toString());
        }
        return answer;
    }
}
