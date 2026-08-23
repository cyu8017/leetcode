// LeetCode 2210 - Count Hills and Valleys in an Array
// https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

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
    int countHillValley(vector<int>& nums) {
        vector<int> compact{nums[0]};
        for (int i = 1; i < (int)nums.size(); i++)
            if (nums[i] != compact.back()) compact.push_back(nums[i]);
        int ans = 0;
        for (int i = 1; i + 1 < (int)compact.size(); i++)
            if ((compact[i] > compact[i - 1] && compact[i] > compact[i + 1]) ||
                (compact[i] < compact[i - 1] && compact[i] < compact[i + 1]))
                ans++;
        return ans;
    }
};
