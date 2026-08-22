// LeetCode 2085 - Count Common Words With One Occurrence
// https://leetcode.com/problems/count-common-words-with-one-occurrence/

#include <string.h>

int countWords(char** words1, int words1Size, char** words2, int words2Size) {
    int ans = 0;
    for (int i = 0; i < words1Size; i++) {
        int c1 = 0, c2 = 0;
        for (int j = 0; j < words1Size; j++) if (strcmp(words1[i], words1[j]) == 0) c1++;
        if (c1 != 1) continue;
        for (int j = 0; j < words2Size; j++) if (strcmp(words1[i], words2[j]) == 0) c2++;
        if (c2 == 1) ans++;
    }
    return ans;
}
