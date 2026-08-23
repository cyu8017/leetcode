// LeetCode 2155 - All Divisions With the Highest Score of a Binary Array
// https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

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
    vector<int> maxScoreIndices(vector<int>& nums) {
        int n = nums.size();
        int total1 = accumulate(nums.begin(), nums.end(), 0);
        int best = total1, left0 = 0, right1 = total1;
        vector<int> ans{0};
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) left0++;
            else right1--;
            int score = left0 + right1;
            if (score > best) { best = score; ans = {i + 1}; }
            else if (score == best) ans.push_back(i + 1);
        }
        return ans;
    }
};
