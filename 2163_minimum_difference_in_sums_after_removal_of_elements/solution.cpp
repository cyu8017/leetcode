// LeetCode 2163 - Minimum Difference in Sums After Removal of Elements
// https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

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
    long long minimumDifference(vector<int>& nums) {
        int n = nums.size() / 3;
        vector<long long> left(nums.size()), right(nums.size());
        priority_queue<int> hmax;
        long long sum = 0;
        for (int i = 0; i < n; i++) { hmax.push(nums[i]); sum += nums[i]; }
        left[n - 1] = sum;
        for (int i = n; i < 2 * n; i++) {
            hmax.push(nums[i]);
            sum += nums[i];
            sum -= hmax.top(); hmax.pop();
            left[i] = sum;
        }
        priority_queue<int, vector<int>, greater<int>> hmin;
        sum = 0;
        for (int i = (int)nums.size() - 1; i >= 2 * n; i--) { hmin.push(nums[i]); sum += nums[i]; }
        right[2 * n] = sum;
        for (int i = 2 * n - 1; i >= n; i--) {
            hmin.push(nums[i]);
            sum += nums[i];
            sum -= hmin.top(); hmin.pop();
            right[i] = sum;
        }
        long long ans = left[n - 1] - right[n];
        for (int i = n; i < 2 * n; i++) ans = min(ans, left[i] - right[i + 1]);
        return ans;
    }
};
