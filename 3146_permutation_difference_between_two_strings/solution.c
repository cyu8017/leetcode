// LeetCode 3146 - Permutation Difference between Two Strings
// https://leetcode.com/problems/permutation-difference-between-two-strings/

int findPermutationDifference(char* s, char* t) {
    int d[26] = {0};
    for (int i = 0; s[i]; i++) d[s[i] - 'a'] = i;
    int ans = 0;
    for (int i = 0; t[i]; i++) {
        int diff = d[t[i] - 'a'] - i;
        if (diff < 0) diff = -diff;
        ans += diff;
    }
    return ans;
}
