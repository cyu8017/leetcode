// LeetCode 2002 - Maximum Product of the Length of Two Palindromic Subsequences
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

#include <algorithm>
#include <array>
#include <bitset>
#include <cmath>
#include <cstdint>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

class Solution {
public:
    int maxProduct(string s) {
        int n = (int)s.size();
        auto isPal = [&](int mask) -> pair<bool,int> {
            string chars;
            for (int i = 0; i < n; i++) if (mask & (1 << i)) chars.push_back(s[i]);
            for (int l = 0, r = (int)chars.size() - 1; l < r; l++, r--)
                if (chars[l] != chars[r]) return {false, 0};
            return {true, (int)chars.size()};
        };
        int best = 0, total = 1 << n;
        for (int mask1 = 1; mask1 < total; mask1++) {
            auto [ok1, len1] = isPal(mask1);
            if (!ok1) continue;
            int remain = (total - 1) ^ mask1;
            for (int mask2 = remain; mask2 > 0; mask2 = (mask2 - 1) & remain) {
                auto [ok2, len2] = isPal(mask2);
                if (ok2 && len1 * len2 > best) best = len1 * len2;
            }
        }
        return best;
    }
};
