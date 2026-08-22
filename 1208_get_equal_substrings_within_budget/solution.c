// LeetCode 1208 - Get Equal Substrings Within Budget
// https://leetcode.com/problems/get-equal-substrings-within-budget/

#include <stdlib.h>
#include <string.h>

int equalSubstring(char* s, char* t, int maxCost) {
    int n = (int)strlen(s);
    int left = 0;
    int cost = 0;
    int answer = 0;
    for (int right = 0; right < n; right++) {
        cost += abs(s[right] - t[right]);
        while (cost > maxCost) {
            cost -= abs(s[left] - t[left]);
            left++;
        }
        if (right - left + 1 > answer) answer = right - left + 1;
    }
    return answer;
}
