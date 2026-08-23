// LeetCode 2172 - Maximum AND Sum of Array
// https://leetcode.com/problems/maximum-and-sum-of-array/

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
    int maximumANDSum(vector<int>& nums, int numSlots) {
        int n = nums.size(), slots = numSlots, maxMask = 1;
        for (int i = 0; i < slots; i++) maxMask *= 3;
        vector<int> dp(maxMask);
        for (int mask = 0; mask < maxMask; mask++) {
            int cnt = 0, x = mask;
            while (x) { cnt += x % 3; x /= 3; }
            if (cnt >= n) continue;
            int v = nums[cnt], base = 1;
            for (int s = 1; s <= slots; s++) {
                int occ = (mask / base) % 3;
                if (occ < 2) {
                    int nm = mask + base;
                    dp[nm] = max(dp[nm], dp[mask] + (v & s));
                }
                base *= 3;
            }
        }
        return *max_element(dp.begin(), dp.end());
    }
};
