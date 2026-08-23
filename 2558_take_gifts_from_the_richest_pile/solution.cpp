// LeetCode 2558 - Take Gifts From the Richest Pile
// https://leetcode.com/problems/take-gifts-from-the-richest-pile/

#include <cmath>
#include <queue>
#include <vector>

class Solution {
public:
    long long pickGifts(std::vector<int>& gifts, int k) {
        std::priority_queue<int> h(gifts.begin(), gifts.end());
        for (int i = 0; i < k; ++i) {
            int x = h.top();
            h.pop();
            h.push((int)std::sqrt(x));
        }
        long long ans = 0;
        while (!h.empty()) {
            ans += h.top();
            h.pop();
        }
        return ans;
    }
};
