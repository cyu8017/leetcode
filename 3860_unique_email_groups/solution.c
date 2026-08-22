// LeetCode 3860 - Unique Email Groups
// https://leetcode.com/problems/unique-email-groups/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int uniqueEmailGroups(char** emails, int emailsSize) {
    char** keys = (char**)malloc((size_t)emailsSize * sizeof(char*));
    int ksz = 0;
    for (int e = 0; e < emailsSize; e++) {
        char* email = emails[e];
        char* at = strchr(email, '@');
        if (!at) continue;
        int localLen = (int)(at - email);
        char local[256];
        int li = 0;
        for (int i = 0; i < localLen; i++) {
            if (email[i] == '+') break;
            if (email[i] == '.') continue;
            local[li++] = (char)tolower((unsigned char)email[i]);
        }
        local[li] = '\0';
        char domain[256];
        int di = 0;
        for (char* p = at + 1; *p; p++) domain[di++] = (char)tolower((unsigned char)*p);
        domain[di] = '\0';
        char* norm = (char*)malloc((size_t)li + di + 1);
        strcpy(norm, local);
        strcat(norm, domain);
        int found = 0;
        for (int i = 0; i < ksz; i++) if (strcmp(keys[i], norm) == 0) { found = 1; break; }
        if (found) free(norm);
        else keys[ksz++] = norm;
    }
    for (int i = 0; i < ksz; i++) free(keys[i]);
    free(keys);
    return ksz;
}
