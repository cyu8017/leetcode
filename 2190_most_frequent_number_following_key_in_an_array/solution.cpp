// LeetCode 2190 - Most Frequent Number Following Key In an Array
// https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

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
    int mostFrequent(vector<int>& nums, int key) {
        unordered_map<int, int> freq;
        int best = 0, ans = 0;
        for (int i = 0; i + 1 < (int)nums.size(); i++) {
            if (nums[i] == key) {
                freq[nums[i + 1]]++;
                if (freq[nums[i + 1]] > best) {
                    best = freq[nums[i + 1]];
                    ans = nums[i + 1];
                }
            }
        }
        return ans;
    }
};
