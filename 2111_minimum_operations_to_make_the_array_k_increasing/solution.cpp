// LeetCode 2111 - Minimum Operations to Make the Array K-Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/

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
    int kIncreasing(vector<int>& arr, int k) {
        int ans = 0, n = arr.size();
        for (int start = 0; start < k; start++) {
            vector<int> seq;
            for (int i = start; i < n; i += k) seq.push_back(arr[i]);
            vector<int> tails;
            for (int x : seq) {
                auto it = upper_bound(tails.begin(), tails.end(), x);
                if (it == tails.end()) tails.push_back(x);
                else *it = x;
            }
            ans += (int)seq.size() - (int)tails.size();
        }
        return ans;
    }
};
