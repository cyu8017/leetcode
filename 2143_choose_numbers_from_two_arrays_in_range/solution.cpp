// LeetCode 2143 - Choose Numbers From Two Arrays in Range
// https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/

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
    int countSubranges(vector<int>& nums1, vector<int>& nums2) {
        const int MOD = 1000000007;
        int n = nums1.size(), ans = 0;
        unordered_map<int, int> dp;
        for (int i = 0; i < n; i++) {
            unordered_map<int, int> ndp;
            ndp[nums1[i]] = (ndp[nums1[i]] + 1) % MOD;
            ndp[-nums2[i]] = (ndp[-nums2[i]] + 1) % MOD;
            for (auto& [diff, cnt] : dp) {
                ndp[diff + nums1[i]] = (ndp[diff + nums1[i]] + cnt) % MOD;
                ndp[diff - nums2[i]] = (ndp[diff - nums2[i]] + cnt) % MOD;
            }
            dp.swap(ndp);
            ans = (ans + dp[0]) % MOD;
        }
        return ans;
    }
};
