// LeetCode 2001 - Number of Pairs of Interchangeable Rectangles
// https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

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
    long long interchangeableRectangles(vector<vector<int>>& rectangles) {
        auto gcd = [](int a, int b) {
            while (b) { int t = a % b; a = b; b = t; }
            return a;
        };
        map<pair<int,int>, int> freq;
        long long ans = 0;
        for (auto& rect : rectangles) {
            int w = rect[0], h = rect[1], g = gcd(w, h);
            pair<int,int> key{w / g, h / g};
            ans += freq[key];
            freq[key]++;
        }
        return ans;
    }
};
