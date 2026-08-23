// LeetCode 2134 - Minimum Swaps to Group All 1's Together II
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

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
    int minSwaps(vector<int>& nums) {
        int ones = accumulate(nums.begin(), nums.end(), 0);
        if (ones == 0) return 0;
        int n = nums.size(), window = 0;
        for (int i = 0; i < ones; i++) window += nums[i];
        int best = window;
        for (int i = 0; i < n; i++) {
            window -= nums[i];
            window += nums[(i + ones) % n];
            best = max(best, window);
        }
        return ones - best;
    }
};
