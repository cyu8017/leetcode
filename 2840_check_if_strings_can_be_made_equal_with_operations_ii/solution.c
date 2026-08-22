// LeetCode 2840 - Check if Strings Can be Made Equal With Operations II
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

#include <stdbool.h>
#include <string.h>

bool checkStrings(char* s1, char* s2) {
    int even1[26]={0}, odd1[26]={0}, even2[26]={0}, odd2[26]={0};
    for (int i = 0; s1[i]; i++) {
        if (i % 2 == 0) { even1[s1[i]-'a']++; even2[s2[i]-'a']++; }
        else { odd1[s1[i]-'a']++; odd2[s2[i]-'a']++; }
    }
    return memcmp(even1, even2, sizeof(even1)) == 0 && memcmp(odd1, odd2, sizeof(odd1)) == 0;
}
