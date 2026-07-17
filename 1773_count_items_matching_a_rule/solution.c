// LeetCode 1773 - Count Items Matching a Rule
// https://leetcode.com/problems/count-items-matching-a-rule/

#include <string.h>

int countMatches(char*** items, int itemsSize, int* itemsColSize, char* ruleKey,
                 char* ruleValue) {
    int idx = strcmp(ruleKey, "type") == 0 ? 0 : strcmp(ruleKey, "color") == 0 ? 1 : 2;
    int count = 0;
    for (int i = 0; i < itemsSize; i++) {
        if (strcmp(items[i][idx], ruleValue) == 0) {
            count++;
        }
    }
    return count;
}
