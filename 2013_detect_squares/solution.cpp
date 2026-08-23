// LeetCode 2013 - Detect Squares
// https://leetcode.com/problems/detect-squares/

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

class DetectSquares {
    map<pair<int,int>, int> cnt;
public:
    DetectSquares() {}
    void add(vector<int> point) { cnt[{point[0], point[1]}]++; }
    int count(vector<int> point) {
        int x = point[0], y = point[1], ans = 0;
        for (auto& [p, c] : cnt) {
            int px = p.first, py = p.second;
            if (px == x || py == y) continue;
            if (abs(px - x) != abs(py - y)) continue;
            ans += c * cnt[{px, y}] * cnt[{x, py}];
        }
        return ans;
    }
};
