// LeetCode 0299 - Bulls and Cows
// https://leetcode.com/problems/bulls-and-cows/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public String getHint(String secret, String guess) {
        int bulls = 0;
        Map<Character, Integer> secretCounts = new HashMap<>();
        Map<Character, Integer> guessCounts = new HashMap<>();
        for (int index = 0; index < secret.length(); index++) {
            char secretDigit = secret.charAt(index);
            char guessDigit = guess.charAt(index);
            if (secretDigit == guessDigit) {
                bulls++;
            } else {
                secretCounts.put(secretDigit, secretCounts.getOrDefault(secretDigit, 0) + 1);
                guessCounts.put(guessDigit, guessCounts.getOrDefault(guessDigit, 0) + 1);
            }
        }
        int cows = 0;
        for (Map.Entry<Character, Integer> entry : guessCounts.entrySet()) {
            cows += Math.min(entry.getValue(), secretCounts.getOrDefault(entry.getKey(), 0));
        }
        return bulls + "A" + cows + "B";
    }
}
