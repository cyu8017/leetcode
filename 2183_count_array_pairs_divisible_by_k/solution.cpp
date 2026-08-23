// LeetCode 2183 - Count Array Pairs Divisible by K
// https://leetcode.com/problems/count-array-pairs-divisible-by-k/

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
    long long countPairs(vector<int>& nums, int k) {
        auto gcd = [](int a, int b) { while (b) { int t = a % b; a = b; b = t; } return a; };
        unordered_map<int, int> freq;
        long long ans = 0;
        for (int x : nums) {
            int g1 = gcd(x, k);
            for (auto& [g2, c] : freq)
                if (1LL * g1 * g2 % k == 0) ans += c;
            freq[g1]++;
        }
        return ans;
    }
};
