// LeetCode 2161 - Partition Array According to Given Pivot
// https://leetcode.com/problems/partition-array-according-to-given-pivot/

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
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> less, eq, greater;
        for (int x : nums) {
            if (x < pivot) less.push_back(x);
            else if (x == pivot) eq.push_back(x);
            else greater.push_back(x);
        }
        less.insert(less.end(), eq.begin(), eq.end());
        less.insert(less.end(), greater.begin(), greater.end());
        return less;
    }
};
