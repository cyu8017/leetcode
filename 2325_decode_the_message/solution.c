// LeetCode 2325 - Decode the Message
// https://leetcode.com/problems/decode-the-message/

#include <stdlib.h>
#include <string.h>

char* decodeMessage(char* key, char* message) {
    char mp[26] = {0};
    char next = 'a';
    for (int i = 0; key[i]; i++) {
        char c = key[i];
        if (c == ' ' || mp[c - 'a'] != 0) continue;
        mp[c - 'a'] = next++;
    }
    int n = (int)strlen(message);
    char* out = (char*)malloc((size_t)n + 1);
    for (int i = 0; i < n; i++) {
        if (message[i] == ' ') out[i] = ' ';
        else out[i] = mp[message[i] - 'a'];
    }
    out[n] = '\0';
    return out;
}
