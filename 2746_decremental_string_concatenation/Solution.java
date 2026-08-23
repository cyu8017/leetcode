// LeetCode 2746 - Decremental String Concatenation
// https://leetcode.com/problems/decremental-string-concatenation/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minimizeConcatenatedLength(String[] words) {
        int n = words.length;
        Map<String, Integer> memo = new HashMap<>();
        String w0 = words[0];
        return w0.length() + dfs(words, 1, w0.charAt(0), w0.charAt(w0.length() - 1), memo);
    }

    private int dfs(String[] words, int i, char first, char last, Map<String, Integer> memo) {
        if (i == words.length) return 0;
        String key = i + "," + first + "," + last;
        if (memo.containsKey(key)) return memo.get(key);
        String w = words[i];
        char wf = w.charAt(0), wl = w.charAt(w.length() - 1);
        int add1 = w.length() - (last == wf ? 1 : 0);
        int add2 = w.length() - (wl == first ? 1 : 0);
        int a = add1 + dfs(words, i + 1, first, wl, memo);
        int b = add2 + dfs(words, i + 1, wf, last, memo);
        int ans = Math.min(a, b);
        memo.put(key, ans);
        return ans;
    }
}
