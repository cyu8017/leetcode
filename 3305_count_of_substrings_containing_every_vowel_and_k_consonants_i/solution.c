// LeetCode 3305 - Count of Substrings Containing Every Vowel and K Consonants I
// https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/

#include <string.h>
#include <stdbool.h>

static bool isVow(char c) {
    return c=='a'||c=='e'||c=='i'||c=='o'||c=='u';
}

static int atLeastVow(char* word, int k) {
    int cnt[128] = {0};
    int distinct = 0, cons = 0, l = 0, ans = 0;
    int n = (int)strlen(word);
    for (int r = 0; r < n; r++) {
        char c = word[r];
        if (isVow(c)) {
            if (cnt[(int)c] == 0) distinct++;
            cnt[(int)c]++;
        } else cons++;
        while (distinct == 5 && cons >= k) {
            ans += n - r;
            char c2 = word[l];
            if (isVow(c2)) {
                cnt[(int)c2]--;
                if (cnt[(int)c2] == 0) distinct--;
            } else cons--;
            l++;
        }
    }
    return ans;
}

int countOfSubstrings(char* word, int k) {
    return atLeastVow(word, k) - atLeastVow(word, k + 1);
}
