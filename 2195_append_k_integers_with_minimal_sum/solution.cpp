// LeetCode 2195 - Append K Integers With Minimal Sum
// https://leetcode.com/problems/append-k-integers-with-minimal-sum/

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
    long long minimalKSum(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        long long ans = 0;
        int prev = 0;
        for (int x : nums) {
            if (x <= prev) continue;
            int start = prev + 1, end = x - 1;
            if (start <= end) {
                int cnt = end - start + 1;
                if (cnt > k) { end = start + k - 1; cnt = k; }
                ans += 1LL * (start + end) * cnt / 2;
                k -= cnt;
                if (k == 0) return ans;
            }
            prev = x;
        }
        long long start = prev + 1, end = start + k - 1;
        ans += (start + end) * k / 2;
        return ans;
    }
};
