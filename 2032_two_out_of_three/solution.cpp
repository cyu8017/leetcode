// LeetCode 2032 - Two Out of Three
// https://leetcode.com/problems/two-out-of-three/

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
    vector<int> twoOutOfThree(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3) {
        unordered_set<int> s0(nums1.begin(), nums1.end()), s1(nums2.begin(), nums2.end()), s2(nums3.begin(), nums3.end());
        vector<int> ans;
        for (int v = 1; v <= 100; v++) {
            int c = s0.count(v) + s1.count(v) + s2.count(v);
            if (c >= 2) ans.push_back(v);
        }
        return ans;
    }
};
