// LeetCode 0914 - X of a Kind in a Deck of Cards
// https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

#include <numeric>
#include <unordered_map>
#include <vector>

class Solution {
public:
    bool hasGroupsSizeX(std::vector<int>& deck) {
        std::unordered_map<int, int> count;
        for (int x : deck) count[x]++;
        int g = 0;
        for (auto& [_, c] : count) g = std::gcd(g, c);
        return g >= 2;
    }
};
