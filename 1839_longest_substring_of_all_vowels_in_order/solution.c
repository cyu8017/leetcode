// LeetCode 1839 - Longest Substring Of All Vowels in Order
// https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

#include <string.h>

int longestBeautifulSubstring(char* word) {
    int n = (int)strlen(word);
    int best = 0;
    int i = 0;
    while (i < n) {
        if (word[i] != 'a') {
            i++;
            continue;
        }
        int j = i;
        int unique = 1;
        while (j + 1 < n && word[j + 1] >= word[j]) {
            if (word[j + 1] > word[j]) unique++;
            j++;
        }
        if (unique == 5 && word[j] == 'u') {
            int len = j - i + 1;
            if (len > best) best = len;
        }
        i = j + 1;
    }
    return best;
}
