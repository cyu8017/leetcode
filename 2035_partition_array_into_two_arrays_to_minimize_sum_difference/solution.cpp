// LeetCode 2035 - Partition Array Into Two Arrays to Minimize Sum Difference
// https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

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
    int minimumDifference(vector<int>& nums) {
        int n = (int)nums.size() / 2;
        int total = accumulate(nums.begin(), nums.end(), 0);
        auto sumsByCount = [&](vector<int>& arr) {
            int m = (int)arr.size();
            vector<vector<int>> res(m + 1);
            for (int mask = 0; mask < (1 << m); mask++) {
                int sum = 0, c = 0;
                for (int i = 0; i < m; i++) if (mask & (1 << i)) { sum += arr[i]; c++; }
                res[c].push_back(sum);
            }
            for (auto& v : res) sort(v.begin(), v.end());
            return res;
        };
        vector<int> left(nums.begin(), nums.begin() + n), right(nums.begin() + n, nums.end());
        auto L = sumsByCount(left), R = sumsByCount(right);
        int ans = INT_MAX;
        for (int k = 0; k <= n; k++) {
            for (int s1 : L[k]) {
                int need = total / 2 - s1;
                auto& arr = R[n - k];
                auto it = lower_bound(arr.begin(), arr.end(), need);
                for (auto idx : {(int)(it - arr.begin()) - 1, (int)(it - arr.begin())}) {
                    if (idx >= 0 && idx < (int)arr.size()) {
                        int s2 = arr[idx];
                        ans = min(ans, abs(total - 2 * (s1 + s2)));
                    }
                }
            }
        }
        return ans;
    }
};
