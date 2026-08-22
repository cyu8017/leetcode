// LeetCode 0383 - Ransom Note
// https://leetcode.com/problems/ransom-note/

#include <stdbool.h>

bool canConstruct(char* ransomNote, char* magazine) {
    int counts[26] = {0};

    for (int index = 0; magazine[index] != '\0'; index++) {
        counts[magazine[index] - 'a'] += 1;
    }

    for (int index = 0; ransomNote[index] != '\0'; index++) {
        if (counts[ransomNote[index] - 'a'] == 0) {
            return false;
        }
        counts[ransomNote[index] - 'a'] -= 1;
    }

    return true;
}
