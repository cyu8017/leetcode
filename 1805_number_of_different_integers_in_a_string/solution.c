// LeetCode 1805 - Number of Different Integers in a String
// https://leetcode.com/problems/number-of-different-integers-in-a-string/

#include <ctype.h>
#include <stdlib.h>
#include <string.h>

static int normEq(const char* a, int alen, const char* b, int blen) {
    while (alen > 1 && a[0] == '0') {
        a++;
        alen--;
    }
    while (blen > 1 && b[0] == '0') {
        b++;
        blen--;
    }
    if (alen != blen) return 0;
    return memcmp(a, b, (size_t)alen) == 0;
}

int numDifferentIntegers(char* word) {
    char** seen = NULL;
    int* lens = NULL;
    int count = 0;
    int capacity = 0;
    int n = (int)strlen(word);
    int i = 0;
    while (i < n) {
        if (!isdigit((unsigned char)word[i])) {
            i++;
            continue;
        }
        int start = i;
        while (i < n && isdigit((unsigned char)word[i])) i++;
        int len = i - start;
        int found = 0;
        for (int j = 0; j < count; j++) {
            if (normEq(seen[j], lens[j], word + start, len)) {
                found = 1;
                break;
            }
        }
        if (!found) {
            if (count == capacity) {
                capacity = capacity ? capacity * 2 : 8;
                seen = (char**)realloc(seen, (size_t)capacity * sizeof(char*));
                lens = (int*)realloc(lens, (size_t)capacity * sizeof(int));
            }
            seen[count] = (char*)malloc((size_t)len + 1);
            memcpy(seen[count], word + start, (size_t)len);
            seen[count][len] = '\0';
            lens[count] = len;
            count++;
        }
    }
    for (int j = 0; j < count; j++) free(seen[j]);
    free(seen);
    free(lens);
    return count;
}
