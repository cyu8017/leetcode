// LeetCode 3083 - Existence of a Substring in a String and Its Reverse
// https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

#include <stdbool.h>
#include <string.h>

bool isSubstringPresent(char* s) {
    bool st[26][26] = {{false}};
    int n = (int)strlen(s);
    for (int i = 0; i < n - 1; i++) st[s[i + 1] - 'a'][s[i] - 'a'] = true;
    for (int i = 0; i < n - 1; i++) if (st[s[i] - 'a'][s[i + 1] - 'a']) return true;
    return false;
}
