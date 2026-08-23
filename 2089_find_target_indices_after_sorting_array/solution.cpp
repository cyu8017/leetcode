// LeetCode 2089 - Find Target Indices After Sorting Array
// https://leetcode.com/problems/find-target-indices-after-sorting-array/

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
    vector<int> targetIndices(vector<int>& nums, int target) {
        int less = 0, eq = 0;
        for (int x : nums) {
            if (x < target) less++;
            else if (x == target) eq++;
        }
        vector<int> ans(eq);
        for (int i = 0; i < eq; i++) ans[i] = less + i;
        return ans;
    }
};
