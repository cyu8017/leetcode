// LeetCode 0691 - Stickers to Spell Word
// https://leetcode.com/problems/stickers-to-spell-word/

import java.util.*;

class Solution {
    private List<Character> chars = new ArrayList<>();
    private List<int[]> sticks = new ArrayList<>();
    private Map<String, Integer> memo = new HashMap<>();

    private String key(int[] state) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < state.length; i++) {
            if (i > 0) sb.append(',');
            sb.append(state[i]);
        }
        return sb.toString();
    }

    private int dfs(int[] state) {
        String k = key(state);
        if (memo.containsKey(k)) return memo.get(k);
        int i = 0;
        while (i < state.length && state[i] == 0) i++;
        if (i == state.length) {
            memo.put(k, 0);
            return 0;
        }
        char first = chars.get(i);
        int best = Integer.MAX_VALUE / 4;
        for (int[] stick : sticks) {
            if (stick[first - 'a'] == 0) continue;
            int[] nxt = state.clone();
            for (int j = 0; j < chars.size(); j++) {
                nxt[j] = Math.max(0, nxt[j] - stick[chars.get(j) - 'a']);
            }
            best = Math.min(best, 1 + dfs(nxt));
        }
        memo.put(k, best);
        return best;
    }

    public int minStickers(String[] stickers, String target) {
        int[] need = new int[26];
        for (char ch : target.toCharArray()) need[ch - 'a']++;
        chars.clear();
        for (int i = 0; i < 26; i++) if (need[i] > 0) chars.add((char) ('a' + i));
        sticks.clear();
        for (String sticker : stickers) {
            int[] counts = new int[26];
            for (char ch : sticker.toCharArray()) counts[ch - 'a']++;
            boolean useful = false;
            for (char ch : chars) if (counts[ch - 'a'] > 0) { useful = true; break; }
            if (useful) sticks.add(counts);
        }
        memo.clear();
        int[] state = new int[chars.size()];
        for (int i = 0; i < chars.size(); i++) state[i] = need[chars.get(i) - 'a'];
        int result = dfs(state);
        return result >= Integer.MAX_VALUE / 4 ? -1 : result;
    }
}
