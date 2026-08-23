// LeetCode 2098 - Subsequence of Size K With the Largest Even Sum
// https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/

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
    long long largestEvenSum(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end(), greater<int>());
        long long sum = 0;
        for (int i = 0; i < k; i++) sum += nums[i];
        if (sum % 2 == 0) return sum;
        long long ans = -1;
        int oddIn = -1, evenIn = -1, oddOut = -1, evenOut = -1;
        for (int i = k - 1; i >= 0; i--) {
            if (nums[i] % 2 && oddIn == -1) oddIn = i;
            if (nums[i] % 2 == 0 && evenIn == -1) evenIn = i;
        }
        for (int i = k; i < (int)nums.size(); i++) {
            if (nums[i] % 2 && oddOut == -1) oddOut = i;
            if (nums[i] % 2 == 0 && evenOut == -1) evenOut = i;
        }
        if (oddIn != -1 && evenOut != -1) ans = max(ans, sum - nums[oddIn] + nums[evenOut]);
        if (evenIn != -1 && oddOut != -1) ans = max(ans, sum - nums[evenIn] + nums[oddOut]);
        return ans;
    }
};
