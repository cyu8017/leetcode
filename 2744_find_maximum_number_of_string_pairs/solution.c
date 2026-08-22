// LeetCode 2744 - Find Maximum Number of String Pairs
// https://leetcode.com/problems/find-maximum-number-of-string-pairs/

#include <stdbool.h>
#include <string.h>

int maximumNumberOfStringPairs(char** words, int wordsSize) {
    bool seen[26][26] = {{0}};
    int ans = 0;
    for (int i = 0; i < wordsSize; i++) {
        int a = words[i][0] - 'a', b = words[i][1] - 'a';
        if (seen[b][a]) {
            ans++;
            seen[b][a] = false;
        } else {
            seen[a][b] = true;
        }
    }
    return ans;
}
