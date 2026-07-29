// LeetCode 0567 - Permutation in String
// https://leetcode.com/problems/permutation-in-string/

#include <stdbool.h>
#include <string.h>

bool checkInclusion(char* s1, char* s2) {
    int n1 = (int)strlen(s1);
    int n2 = (int)strlen(s2);
    if (n1 > n2) {
        return false;
    }

    int need[26] = {0};
    int window[26] = {0};
    for (int i = 0; i < n1; i++) {
        need[s1[i] - 'a']++;
        window[s2[i] - 'a']++;
    }

    int matches = 0;
    for (int i = 0; i < 26; i++) {
        if (need[i] == window[i]) {
            matches++;
        }
    }
    if (matches == 26) {
        return true;
    }

    for (int right = n1; right < n2; right++) {
        int add = s2[right] - 'a';
        int remove = s2[right - n1] - 'a';

        if (window[add] == need[add]) {
            matches--;
        }
        window[add]++;
        if (window[add] == need[add]) {
            matches++;
        }

        if (window[remove] == need[remove]) {
            matches--;
        }
        window[remove]--;
        if (window[remove] == need[remove]) {
            matches++;
        }

        if (matches == 26) {
            return true;
        }
    }
    return false;
}
