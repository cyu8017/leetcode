// LeetCode 2025 - Maximum Number of Ways to Partition an Array
// https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

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
    int waysToPartition(vector<int>& nums, int k) {
        int n = (int)nums.size();
        vector<long long> pref(n);
        pref[0] = nums[0];
        for (int i = 1; i < n; i++) pref[i] = pref[i - 1] + nums[i];
        long long total = pref[n - 1];
        unordered_map<long long, int> right, left;
        for (int i = 0; i < n - 1; i++) right[pref[i]]++;
        int ans = 0;
        if (total % 2 == 0) ans = right[total / 2];
        for (int i = 0; i < n; i++) {
            long long diff = (long long)k - nums[i];
            long long newTotal = total + diff;
            int cur = 0;
            if (newTotal % 2 == 0) {
                long long half = newTotal / 2;
                cur = left[half] + right[half - diff];
            }
            ans = max(ans, cur);
            if (i < n - 1) {
                left[pref[i]]++;
                right[pref[i]]--;
            }
        }
        return ans;
    }
};
