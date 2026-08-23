// LeetCode 2023 - Number of Pairs of Strings With Concatenation Equal to Target
// https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

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
    int numOfPairs(vector<string>& nums, string target) {
        int ans = 0;
        for (int i = 0; i < (int)nums.size(); i++)
            for (int j = 0; j < (int)nums.size(); j++)
                if (i != j && nums[i] + nums[j] == target) ans++;
        return ans;
    }
};
