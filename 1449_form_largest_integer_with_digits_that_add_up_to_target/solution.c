// LeetCode 1449 - Form Largest Integer With Digits That Add up to Target
// https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/

#include <stdlib.h>
#include <string.h>

char* largestNumber(int* cost, int costSize, int target) {
    (void)costSize;
    char** dp = (char**)calloc(target + 1, sizeof(char*));
    dp[0] = (char*)malloc(1); dp[0][0] = '\0';
    for (int total = 1; total <= target; total++) {
        char* best = NULL;
        for (int digit = 1; digit <= 9; digit++) {
            int price = cost[digit - 1];
            if (total >= price && dp[total - price]) {
                int len = (int)strlen(dp[total - price]);
                char* candidate = (char*)malloc(len + 2);
                candidate[0] = '0' + digit;
                strcpy(candidate + 1, dp[total - price]);
                if (!best || strlen(candidate) > strlen(best) ||
                    (strlen(candidate) == strlen(best) && strcmp(candidate, best) > 0)) {
                    free(best);
                    best = candidate;
                } else free(candidate);
            }
        }
        dp[total] = best;
    }
    char* ans;
    if (dp[target]) {
        ans = (char*)malloc(strlen(dp[target]) + 1);
        strcpy(ans, dp[target]);
    } else {
        ans = (char*)malloc(2); strcpy(ans, "0");
    }
    for (int i = 0; i <= target; i++) free(dp[i]);
    free(dp);
    return ans;
}
