// LeetCode 2483 - Minimum Penalty for a Shop
// https://leetcode.com/problems/minimum-penalty-for-a-shop/

#include <string>

class Solution {
public:
    int bestClosingTime(std::string customers) {
        int n = (int)customers.size();
        int penalty = 0;
        for (char c : customers) if (c == 'Y') penalty++;
        int best = penalty, ans = 0;
        for (int i = 0; i < n; i++) {
            if (customers[i] == 'Y') penalty--;
            else penalty++;
            if (penalty < best) {
                best = penalty;
                ans = i + 1;
            }
        }
        return ans;
    }
};
