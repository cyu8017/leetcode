// LeetCode 2099 - Find Subsequence of Length K With the Largest Sum
// https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

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
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        vector<pair<int,int>> arr;
        for (int i = 0; i < (int)nums.size(); i++) arr.push_back({nums[i], i});
        sort(arr.begin(), arr.end(), [](auto& a, auto& b) { return a.first > b.first; });
        vector<int> idx(k);
        for (int i = 0; i < k; i++) idx[i] = arr[i].second;
        sort(idx.begin(), idx.end());
        vector<int> ans(k);
        for (int i = 0; i < k; i++) ans[i] = nums[idx[i]];
        return ans;
    }
};
