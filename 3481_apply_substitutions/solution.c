// LeetCode 3481 - Apply Substitutions
// https://leetcode.com/problems/apply-substitutions/

#include <stdlib.h>
#include <string.h>

static char* mp_keys[26];
static char* mp_vals[26];
static int mp_n;

static char* resolve(const char* s) {
    int len = (int)strlen(s);
    char* out = (char*)malloc((size_t)len * 64 + 1);
    int oi = 0;
    for (int i = 0; s[i];) {
        if (s[i] == '%') {
            int j = i + 1;
            while (s[j] && s[j] != '%') j++;
            char key[8];
            int kl = j - (i + 1);
            memcpy(key, s + i + 1, (size_t)kl);
            key[kl] = '\0';
            char* val = NULL;
            for (int t = 0; t < mp_n; t++) {
                if (strcmp(mp_keys[t], key) == 0) {
                    val = mp_vals[t];
                    break;
                }
            }
            if (val) {
                char* sub = resolve(val);
                int sl = (int)strlen(sub);
                memcpy(out + oi, sub, (size_t)sl);
                oi += sl;
                free(sub);
            }
            i = j + 1;
        } else {
            out[oi++] = s[i++];
        }
    }
    out[oi] = '\0';
    return out;
}

char* applySubstitutions(char*** replacements, int replacementsSize, int* replacementsColSize, char* text) {
    (void)replacementsColSize;
    mp_n = replacementsSize;
    for (int i = 0; i < replacementsSize; i++) {
        mp_keys[i] = replacements[i][0];
        mp_vals[i] = replacements[i][1];
    }
    return resolve(text);
}
