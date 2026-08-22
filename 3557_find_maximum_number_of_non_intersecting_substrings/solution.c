// LeetCode 3557 - Find Maximum Number of Non Intersecting Substrings
// https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

#include <string.h>

int maxSubstrings(char* word) {
    int ans = 0;
    int first[26];
    for (int i = 0; i < 26; i++) first[i] = -1;
    for (int i = 0; word[i]; i++) {
        int c = word[i] - 'a';
        if (first[c] < 0) first[c] = i;
        else if (i - first[c] + 1 >= 4) {
            ans++;
            for (int j = 0; j < 26; j++) first[j] = -1;
        }
    }
    return ans;
}
