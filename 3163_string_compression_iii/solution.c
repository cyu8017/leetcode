// LeetCode 3163 - String Compression III
// https://leetcode.com/problems/string-compression-iii/

#include <stdlib.h>
#include <string.h>

char* compressedString(char* word) {
    int n = (int)strlen(word);
    char* ans = malloc(n * 2 + 1);
    int p = 0;
    for (int i = 0; i < n; ) {
        int j = i + 1;
        while (j < n && word[j] == word[i]) j++;
        int k = j - i;
        while (k > 0) {
            int x = k > 9 ? 9 : k;
            ans[p++] = '0' + x;
            ans[p++] = word[i];
            k -= x;
        }
        i = j;
    }
    ans[p] = 0;
    return ans;
}
