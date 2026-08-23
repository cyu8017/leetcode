// LeetCode 1839 - Longest Substring Of All Vowels in Order
// https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

class Solution {
    public int longestBeautifulSubstring(String word) {
        String vowels = "aeiou";
        int best = 0;

        for (int start = 0; start < word.length(); start++) {
            if (word.charAt(start) != 'a') {
                continue;
            }

            int[] counts = new int[5];
            for (int end = start; end < word.length(); end++) {
                char current = word.charAt(end);
                if (end > start && current < word.charAt(end - 1)) {
                    break;
                }

                int idx = vowels.indexOf(current);
                counts[idx]++;
                if (idx > 0 && counts[idx - 1] == 0) {
                    break;
                }

                boolean allPresent = true;
                for (int count : counts) {
                    if (count == 0) {
                        allPresent = false;
                        break;
                    }
                }
                if (allPresent) {
                    best = Math.max(best, end - start + 1);
                }
            }
        }

        return best;
    }
}
