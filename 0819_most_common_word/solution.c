// LeetCode 0819 - Most Common Word
// https://leetcode.com/problems/most-common-word/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

char* mostCommonWord(char* paragraph, char** banned, int bannedSize) {
    typedef struct { char w[101]; int c; } Ent;
    Ent ents[1000];
    int nent = 0;
    char word[101];
    int wi = 0;
    for (int i = 0; ; i++) {
        char ch = paragraph[i];
        if (ch && isalpha((unsigned char)ch)) {
            word[wi++] = (char)tolower((unsigned char)ch);
        } else {
            if (wi > 0) {
                word[wi] = '\0';
                bool ban = false;
                for (int b = 0; b < bannedSize; b++)
                    if (strcmp(word, banned[b]) == 0) { ban = true; break; }
                if (!ban) {
                    int found = -1;
                    for (int e = 0; e < nent; e++)
                        if (strcmp(ents[e].w, word) == 0) { found = e; break; }
                    if (found >= 0) ents[found].c++;
                    else { strcpy(ents[nent].w, word); ents[nent].c = 1; nent++; }
                }
                wi = 0;
            }
            if (!ch) break;
        }
    }
    int best = 0;
    for (int i = 1; i < nent; i++) if (ents[i].c > ents[best].c) best = i;
    char* ans = (char*)malloc(strlen(ents[best].w) + 1);
    strcpy(ans, ents[best].w);
    return ans;
}
