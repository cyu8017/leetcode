// LeetCode 2012 - Sum of Beauty in the Array
// https://leetcode.com/problems/sum-of-beauty-in-the-array/

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
    int sumOfBeauties(vector<int>& nums) {
        int n = (int)nums.size();
        vector<int> prefixMax(n), suffixMin(n);
        prefixMax[0] = nums[0];
        for (int i = 1; i < n; i++) prefixMax[i] = max(prefixMax[i - 1], nums[i]);
        suffixMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) suffixMin[i] = min(suffixMin[i + 1], nums[i]);
        int ans = 0;
        for (int i = 1; i < n - 1; i++) {
            if (prefixMax[i - 1] < nums[i] && nums[i] < suffixMin[i + 1]) ans += 2;
            else if (nums[i - 1] < nums[i] && nums[i] < nums[i + 1]) ans++;
        }
        return ans;
    }
};
