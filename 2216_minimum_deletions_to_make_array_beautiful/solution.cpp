// LeetCode 2216 - Minimum Deletions to Make Array Beautiful
// https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/

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
    int minDeletion(vector<int>& nums) {
        int ans = 0, i = 0, n = nums.size();
        while (i + 1 < n) {
            if (nums[i] == nums[i + 1]) { ans++; i++; }
            else i += 2;
        }
        if ((n - ans) % 2) ans++;
        return ans;
    }
};
