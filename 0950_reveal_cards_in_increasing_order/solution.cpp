// LeetCode 0950 - Reveal Cards In Increasing Order
// https://leetcode.com/problems/reveal-cards-in-increasing-order/

#include <algorithm>
#include <deque>
#include <vector>

class Solution {
public:
    std::vector<int> deckRevealedIncreasing(std::vector<int>& deck) {
        std::sort(deck.begin(), deck.end());
        int n = (int)deck.size();
        std::deque<int> idx;
        for (int i = 0; i < n; i++) idx.push_back(i);
        std::vector<int> ans(n);
        for (int card : deck) {
            ans[idx.front()] = card;
            idx.pop_front();
            if (!idx.empty()) {
                idx.push_back(idx.front());
                idx.pop_front();
            }
        }
        return ans;
    }
};
