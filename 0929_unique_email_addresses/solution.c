// LeetCode 0929 - Unique Email Addresses
// https://leetcode.com/problems/unique-email-addresses/

#define _POSIX_C_SOURCE 200809L
#include <stdlib.h>
#include <string.h>

int numUniqueEmails(char** emails, int emailsSize) {
    char** set = (char**)malloc((size_t)emailsSize * sizeof(char*));
    int n = 0;
    for (int i = 0; i < emailsSize; i++) {
        char buf[200];
        int bi = 0;
        char* at = strchr(emails[i], '@');
        for (char* p = emails[i]; p < at; p++) {
            if (*p == '+') break;
            if (*p != '.') buf[bi++] = *p;
        }
        strcpy(buf + bi, at);
        int found = 0;
        for (int j = 0; j < n; j++) if (strcmp(set[j], buf) == 0) { found = 1; break; }
        if (!found) set[n++] = strdup(buf);
    }
    for (int i = 0; i < n; i++) free(set[i]);
    free(set);
    return n;
}
