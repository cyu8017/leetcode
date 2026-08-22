// LeetCode 1807 - Evaluate the Bracket Pairs of a String
// https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

#include <stdlib.h>
#include <string.h>

char* evaluate(char* s, char*** knowledge, int knowledgeSize, int* knowledgeColSize) {
    (void)knowledgeColSize;
    int n = (int)strlen(s);
    char* result = (char*)malloc((size_t)n * 100 + 8);
    int pos = 0;
    for (int i = 0; s[i];) {
        if (s[i] == '(') {
            int j = i + 1;
            while (s[j] != ')') j++;
            int keyLen = j - i - 1;
            const char* value = "?";
            for (int k = 0; k < knowledgeSize; k++) {
                if ((int)strlen(knowledge[k][0]) == keyLen &&
                    memcmp(knowledge[k][0], s + i + 1, (size_t)keyLen) == 0) {
                    value = knowledge[k][1];
                    break;
                }
            }
            int vlen = (int)strlen(value);
            memcpy(result + pos, value, (size_t)vlen);
            pos += vlen;
            i = j + 1;
        } else {
            result[pos++] = s[i++];
        }
    }
    result[pos] = '\0';
    return result;
}
