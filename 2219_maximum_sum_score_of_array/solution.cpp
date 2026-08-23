// LeetCode 2219 - Maximum Sum Score of Array
// https://leetcode.com/problems/maximum-sum-score-of-array/

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
    long long maximumSumScore(vector<int>& nums) {
        long long total = 0, pref = 0;
        for (int x : nums) total += x;
        long long ans = LLONG_MIN;
        for (int x : nums) {
            pref += x;
            ans = max(ans, max(pref, total - pref + x));
        }
        return ans;
    }
};
