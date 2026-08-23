// LeetCode 2036 - Maximum Alternating Subarray Sum
// https://leetcode.com/problems/maximum-alternating-subarray-sum/

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
    long long maximumAlternatingSubarraySum(vector<int>& nums) {
        long long ans = LLONG_MIN, even = 0, odd = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            long long x = nums[i];
            if (i % 2 == 0) even += x;
            else even = max(0LL, even - x);
            ans = max(ans, even);
        }
        even = 0;
        for (int i = 1; i < (int)nums.size(); i++) {
            long long x = nums[i];
            if (i % 2 == 1) odd += x;
            else odd = max(0LL, odd - x);
            ans = max(ans, odd);
        }
        return ans;
    }
};
