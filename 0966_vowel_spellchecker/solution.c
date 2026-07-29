// LeetCode 0966 - Vowel Spellchecker
// https://leetcode.com/problems/vowel-spellchecker/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

static bool isVowel(char c) {
    c = (char)tolower((unsigned char)c);
    return c=='a'||c=='e'||c=='i'||c=='o'||c=='u';
}

static void toLowerStr(const char* s, char* out) {
    int i = 0; for (; s[i]; i++) out[i] = (char)tolower((unsigned char)s[i]); out[i]=0;
}

static void devowel(const char* s, char* out) {
    int i = 0; for (; s[i]; i++) {
        char c = (char)tolower((unsigned char)s[i]);
        out[i] = isVowel(c) ? '*' : c;
    }
    out[i]=0;
}

char** spellchecker(char** wordlist, int wordlistSize, char** queries, int queriesSize, int* returnSize) {
    char** ans = (char**)malloc((size_t)queriesSize * sizeof(char*));
    for (int qi = 0; qi < queriesSize; qi++) {
        char* q = queries[qi];
        char* found = NULL;
        for (int i = 0; i < wordlistSize; i++) if (strcmp(wordlist[i], q) == 0) { found = wordlist[i]; break; }
        if (found) { ans[qi] = found; continue; }
        char ql[100], wl[100];
        toLowerStr(q, ql);
        for (int i = 0; i < wordlistSize; i++) {
            toLowerStr(wordlist[i], wl);
            if (strcmp(wl, ql) == 0) { found = wordlist[i]; break; }
        }
        if (found) { ans[qi] = found; continue; }
        char qd[100], wd[100];
        devowel(q, qd);
        for (int i = 0; i < wordlistSize; i++) {
            devowel(wordlist[i], wd);
            if (strcmp(wd, qd) == 0) { found = wordlist[i]; break; }
        }
        ans[qi] = found ? found : "";
    }
    *returnSize = queriesSize;
    return ans;
}
