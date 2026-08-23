// LeetCode 2113 - Elements in Array After Removing and Replacing Elements
// https://leetcode.com/problems/elements-in-array-after-removing-and-replacing-elements/

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
    vector<int> elementInNums(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int t = queries[i][0], idx = queries[i][1];
            int cycle = t % (2 * n);
            int size, offset;
            if (cycle < n) {
                size = n - cycle;
                offset = cycle;
            } else {
                size = cycle - n;
                offset = 0;
            }
            ans[i] = idx >= size ? -1 : nums[offset + idx];
        }
        return ans;
    }
};
