// LeetCode 2090 - K Radius Subarray Averages
// https://leetcode.com/problems/k-radius-subarray-averages/

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
    vector<int> getAverages(vector<int>& nums, int k) {
        int n = (int)nums.size();
        vector<int> ans(n, -1);
        if (2 * k + 1 > n) return ans;
        long long sum = 0;
        for (int i = 0; i < 2 * k + 1; i++) sum += nums[i];
        ans[k] = (int)(sum / (2 * k + 1));
        for (int i = k + 1; i + k < n; i++) {
            sum += nums[i + k] - nums[i - k - 1];
            ans[i] = (int)(sum / (2 * k + 1));
        }
        return ans;
    }
};
