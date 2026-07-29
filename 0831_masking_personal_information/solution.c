// LeetCode 0831 - Masking Personal Information
// https://leetcode.com/problems/masking-personal-information/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>

char* maskPII(char* s) {
    char* at = strchr(s, '@');
    if (at) {
        char lower[120];
        for (int i = 0; s[i]; i++) lower[i] = (char)tolower((unsigned char)s[i]);
        lower[strlen(s)] = '\0';
        at = strchr(lower, '@');
        char* ans = (char*)malloc(140);
        sprintf(ans, "%c*****%c@%s", lower[0], *(at - 1), at + 1);
        return ans;
    }
    char digits[32];
    int nd = 0;
    for (int i = 0; s[i]; i++) if (isdigit((unsigned char)s[i])) digits[nd++] = s[i];
    digits[nd] = '\0';
    char local[5];
    memcpy(local, digits + nd - 4, 4);
    local[4] = '\0';
    int country = nd - 10;
    char* ans = (char*)malloc(40);
    if (country == 0) sprintf(ans, "***-***-%s", local);
    else {
        char stars[20];
        for (int i = 0; i < country; i++) stars[i] = '*';
        stars[country] = '\0';
        sprintf(ans, "+%s-***-***-%s", stars, local);
    }
    return ans;
}
