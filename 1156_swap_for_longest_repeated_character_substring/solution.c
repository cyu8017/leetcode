// LeetCode 1156 - Swap For Longest Repeated Character Substring
// https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

#include <string.h>

int maxRepOpt1(char* text) {
    int count[26] = {0};
    int n = (int)strlen(text);
    for (int i = 0; i < n; i++) count[text[i] - 'a']++;
    int ans = 0, i = 0;
    while (i < n) {
        int j = i;
        while (j < n && text[j] == text[i]) j++;
        int length = j - i;
        int k = j + 1;
        while (k < n && text[k] == text[i]) k++;
        int length2 = j < n ? k - j - 1 : 0;
        int cand = length + length2 + 1;
        if (cand > count[text[i] - 'a']) cand = count[text[i] - 'a'];
        if (cand > ans) ans = cand;
        i = j;
    }
    return ans;
}
