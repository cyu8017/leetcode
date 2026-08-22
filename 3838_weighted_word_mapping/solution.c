// LeetCode 3838 - Weighted Word Mapping
// https://leetcode.com/problems/weighted-word-mapping/

#include <stdlib.h>
#include <string.h>

char* mapWordWeights(char** words, int wordsSize, int* weights, int weightsSize) {
    (void)weightsSize;
    char* ans = (char*)malloc((size_t)wordsSize + 1);
    for (int wi = 0; wi < wordsSize; wi++) {
        char* w = words[wi];
        int s = 0;
        for (int i = 0; w[i]; i++) s = (s + weights[w[i] - 'a']) % 26;
        ans[wi] = (char)('a' + (25 - s));
    }
    ans[wordsSize] = '\0';
    return ans;
}
