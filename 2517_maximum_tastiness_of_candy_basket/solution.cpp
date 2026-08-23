// LeetCode 2517 - Maximum Tastiness of Candy Basket
// https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximumTastiness(std::vector<int>& price, int k) {
        std::sort(price.begin(), price.end());
        auto ok = [&](int d) {
            int cnt = 1, last = price[0];
            for (int i = 1; i < (int)price.size(); i++) {
                if (price[i] - last >= d) {
                    cnt++;
                    last = price[i];
                    if (cnt >= k) return true;
                }
            }
            return false;
        };
        int lo = 0, hi = price.back() - price[0];
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};
