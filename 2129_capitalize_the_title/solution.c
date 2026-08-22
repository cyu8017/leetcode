// LeetCode 2129 - Capitalize the Title
// https://leetcode.com/problems/capitalize-the-title/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char* capitalizeTitle(char* title) {
    int n = (int)strlen(title);
    char* out = (char*)malloc((size_t)n + 1);
    int oi = 0, i = 0;
    while (title[i]) {
        while (title[i] == ' ') { out[oi++] = ' '; i++; }
        if (!title[i]) break;
        int start = i;
        while (title[i] && title[i] != ' ') i++;
        int len = i - start;
        for (int k = 0; k < len; k++) {
            char c = (char)tolower((unsigned char)title[start + k]);
            if (len > 2 && k == 0) c = (char)toupper((unsigned char)c);
            out[oi++] = c;
        }
    }
    out[oi] = '\0';
    return out;
}
