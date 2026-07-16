// LeetCode 0424 - Longest Repeating Character Replacement
// https://leetcode.com/problems/longest-repeating-character-replacement/

public class Solution {
    public int CharacterReplacement(string s, int k) {
        int[] counts = new int[26];
        int left = 0;
        int best = 0;
        int maxCount = 0;

        for (int right = 0; right < s.Length; right++) {
            int index = s[right] - 'A';
            counts[index]++;
            maxCount = int.Max(maxCount, counts[index]);
            while ((right - left + 1) - maxCount > k) {
                int leftIndex = s[left] - 'A';
                counts[leftIndex]--;
                left++;
            }
            best = int.Max(best, right - left + 1);
        }

        return best;
    }
}
