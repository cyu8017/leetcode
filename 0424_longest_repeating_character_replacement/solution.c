// LeetCode 0424 - Longest Repeating Character Replacement
// https://leetcode.com/problems/longest-repeating-character-replacement/

int characterReplacement(char* s, int k) {
    int counts[26] = {0};
    int left = 0;
    int best = 0;
    int maxCount = 0;

    for (int right = 0; s[right]; right++) {
        int idx = s[right] - 'A';
        counts[idx]++;
        if (counts[idx] > maxCount) {
            maxCount = counts[idx];
        }
        while ((right - left + 1) - maxCount > k) {
            counts[s[left] - 'A']--;
            left++;
        }
        int window = right - left + 1;
        if (window > best) {
            best = window;
        }
    }
    return best;
}
