// LeetCode 2214 - Minimum Health to Beat Game
// https://leetcode.com/problems/minimum-health-to-beat-game/

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
    long long minimumHealth(vector<int>& damage, int armor) {
        long long sum = 0;
        int mx = 0;
        for (int d : damage) { sum += d; mx = max(mx, d); }
        return sum - min(armor, mx) + 1;
    }
};
