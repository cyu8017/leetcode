// LeetCode 0522 - Longest Uncommon Subsequence II
// https://leetcode.com/problems/longest-uncommon-subsequence-ii/

#include <stdbool.h>
#include <string.h>

static bool isSubsequence(const char* target, const char* source) {
    int index = 0;
    const int targetLength = (int)strlen(target);
    for (int sourceIndex = 0; source[sourceIndex] != '\0'; sourceIndex++) {
        if (index < targetLength && target[index] == source[sourceIndex]) {
            index++;
        }
    }
    return index == targetLength;
}

int findLUSlength(char** strs, int strsSize) {
    int result = -1;
    for (int i = 0; i < strsSize; i++) {
        bool uncommon = true;
        for (int j = 0; j < strsSize; j++) {
            if (i != j && isSubsequence(strs[i], strs[j])) {
                uncommon = false;
                break;
            }
        }
        if (uncommon) {
            const int length = (int)strlen(strs[i]);
            if (length > result) {
                result = length;
            }
        }
    }
    return result;
}
