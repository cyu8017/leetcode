// LeetCode 1153 - String Transforms Into Another String
// https://leetcode.com/problems/string-transforms-into-another-string/

#include <stdbool.h>
#include <string.h>

bool canConvert(char* str1, char* str2) {
    if (strcmp(str1, str2) == 0) return true;
    char map[26];
    memset(map, 0, sizeof(map));
    bool used[26] = {false};
    int n = (int)strlen(str1);
    for (int i = 0; i < n; i++) {
        int a = str1[i] - 'a', b = str2[i] - 'a';
        if (map[a] && map[a] != str2[i]) return false;
        map[a] = str2[i];
        used[b] = true;
    }
    int distinct = 0;
    for (int i = 0; i < 26; i++) if (used[i]) distinct++;
    return distinct < 26;
}
