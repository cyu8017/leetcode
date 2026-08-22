// LeetCode 2186 - Minimum Number of Steps to Make Two Strings Anagram II
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

int minSteps(char* s, char* t) {
    int freq[26] = {0};
    for (int i = 0; s[i]; i++) freq[s[i] - 'a']++;
    for (int i = 0; t[i]; i++) freq[t[i] - 'a']--;
    int ans = 0;
    for (int i = 0; i < 26; i++) ans += freq[i] > 0 ? freq[i] : -freq[i];
    return ans;
}
