// LeetCode 0242 - Valid Anagram
// https://leetcode.com/problems/valid-anagram/

#include <stdbool.h>
#include <string.h>

bool isAnagram(char* s, char* t) {
    if (strlen(s) != strlen(t)) {
        return false;
    }
    int counts[26] = {0};
    for (int index = 0; s[index] != '\0'; ++index) {
        counts[s[index] - 'a']++;
        counts[t[index] - 'a']--;
    }
    for (int index = 0; index < 26; ++index) {
        if (counts[index] != 0) {
            return false;
        }
    }
    return true;
}
