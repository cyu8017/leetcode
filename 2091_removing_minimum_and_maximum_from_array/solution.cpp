// LeetCode 2091 - Removing Minimum and Maximum From Array
// https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

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
    int minimumDeletions(vector<int>& nums) {
        int n = (int)nums.size(), mi = 0, ma = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] < nums[mi]) mi = i;
            if (nums[i] > nums[ma]) ma = i;
        }
        if (mi > ma) swap(mi, ma);
        return min({ma + 1, n - mi, mi + 1 + n - ma});
    }
};
