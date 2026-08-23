// LeetCode 0748 - Shortest Completing Word
// https://leetcode.com/problems/shortest-completing-word/

class Solution {
    public String shortestCompletingWord(String licensePlate, String[] words) {
        int[] need = new int[26];
        for (char ch : licensePlate.toCharArray()) {
            if (Character.isLetter(ch)) need[Character.toLowerCase(ch) - 'a']++;
        }
        String best = "";
        for (String word : words) {
            int[] counts = new int[26];
            for (char ch : word.toCharArray()) counts[ch - 'a']++;
            boolean ok = true;
            for (int i = 0; i < 26; i++) if (counts[i] < need[i]) { ok = false; break; }
            if (ok && (best.isEmpty() || word.length() < best.length())) best = word;
        }
        return best;
    }
}
