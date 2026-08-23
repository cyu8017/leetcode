// LeetCode 2048 - Next Greater Numerically Balanced Number
// https://leetcode.com/problems/next-greater-numerically-balanced-number/

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
    int nextBeautifulNumber(int n) {
        auto balanced = [](int x) {
            int cnt[10] = {};
            while (x) { cnt[x % 10]++; x /= 10; }
            for (int d = 0; d < 10; d++) if (cnt[d] && cnt[d] != d) return false;
            return true;
        };
        for (int x = n + 1; ; x++) if (balanced(x)) return x;
    }
};
