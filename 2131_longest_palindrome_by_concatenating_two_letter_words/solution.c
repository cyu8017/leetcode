// LeetCode 2131 - Longest Palindrome by Concatenating Two Letter Words
// https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

int longestPalindrome(char** words, int wordsSize) {
    int freq[26][26] = {0};
    for (int i = 0; i < wordsSize; i++) {
        freq[words[i][0] - 'a'][words[i][1] - 'a']++;
    }
    int ans = 0, center = 0;
    for (int i = 0; i < 26; i++) {
        for (int j = 0; j < 26; j++) {
            if (i == j) {
                ans += (freq[i][j] / 2) * 4;
                if (freq[i][j] % 2) center = 1;
            } else if (i < j) {
                int use = freq[i][j] < freq[j][i] ? freq[i][j] : freq[j][i];
                ans += use * 4;
            }
        }
    }
    if (center) ans += 2;
    return ans;
}
