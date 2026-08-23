// LeetCode 2200 - Find All K-Distant Indices in an Array
// https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

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
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        int n = nums.size();
        vector<char> mark(n);
        for (int i = 0; i < n; i++) {
            if (nums[i] == key) {
                int l = max(0, i - k), r = min(n - 1, i + k);
                for (int j = l; j <= r; j++) mark[j] = 1;
            }
        }
        vector<int> ans;
        for (int i = 0; i < n; i++) if (mark[i]) ans.push_back(i);
        return ans;
    }
};
