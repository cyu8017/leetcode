// LeetCode 2483 - Minimum Penalty for a Shop
// https://leetcode.com/problems/minimum-penalty-for-a-shop/

#include <string.h>

int bestClosingTime(char* customers) {
    int n = (int)strlen(customers);
    int penalty = 0;
    for (int i = 0; i < n; i++) if (customers[i] == 'Y') penalty++;
    int best = penalty, ans = 0;
    for (int i = 0; i < n; i++) {
        if (customers[i] == 'Y') penalty--;
        else penalty++;
        if (penalty < best) { best = penalty; ans = i + 1; }
    }
    return ans;
}
