// LeetCode 3541 - Find Most Frequent Vowel and Consonant
// https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

#include <string.h>

int maxFreqSum(char* s) {
    int cnt[26] = {0};
    for (int i = 0; s[i]; i++) cnt[s[i] - 'a']++;
    int mv = 0, mc = 0;
    for (int i = 0; i < 26; i++) {
        char c = (char)('a' + i);
        int isV = (c=='a'||c=='e'||c=='i'||c=='o'||c=='u');
        if (isV) { if (cnt[i] > mv) mv = cnt[i]; }
        else { if (cnt[i] > mc) mc = cnt[i]; }
    }
    return mv + mc;
}
