// LeetCode 2044 - Count Number of Maximum Bitwise-OR Subsets
// https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

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
    int countMaxOrSubsets(vector<int>& nums) {
        int maxOr = 0, ans = 0;
        for (int x : nums) maxOr |= x;
        function<void(int,int)> dfs = [&](int i, int cur) {
            if (i == (int)nums.size()) { if (cur == maxOr) ans++; return; }
            dfs(i + 1, cur);
            dfs(i + 1, cur | nums[i]);
        };
        dfs(0, 0);
        return ans;
    }
};
