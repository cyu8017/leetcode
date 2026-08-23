// LeetCode 2191 - Sort the Jumbled Numbers
// https://leetcode.com/problems/sort-the-jumbled-numbers/

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
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        auto mapVal = [&](int x) {
            if (x == 0) return mapping[0];
            vector<int> digits;
            while (x > 0) { digits.push_back(x % 10); x /= 10; }
            int res = 0;
            for (int i = (int)digits.size() - 1; i >= 0; i--)
                res = res * 10 + mapping[digits[i]];
            return res;
        };
        vector<array<int,3>> arr(nums.size());
        for (int i = 0; i < (int)nums.size(); i++)
            arr[i] = {mapVal(nums[i]), i, nums[i]};
        sort(arr.begin(), arr.end());
        vector<int> ans(nums.size());
        for (int i = 0; i < (int)arr.size(); i++) ans[i] = arr[i][2];
        return ans;
    }
};
