// LeetCode 2208 - Minimum Operations to Halve Array Sum
// https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

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
    int halveArray(vector<int>& nums) {
        priority_queue<double> h;
        double sum = 0;
        for (int x : nums) { h.push(x); sum += x; }
        double target = sum / 2;
        int ans = 0;
        while (sum > target) {
            double x = h.top() / 2; h.pop();
            sum -= x;
            h.push(x);
            ans++;
        }
        return ans;
    }
};
