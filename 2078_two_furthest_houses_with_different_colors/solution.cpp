// LeetCode 2078 - Two Furthest Houses With Different Colors
// https://leetcode.com/problems/two-furthest-houses-with-different-colors/

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
    int maxDistance(vector<int>& colors) {
        int n = (int)colors.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            if (colors[i] != colors[0]) ans = max(ans, i);
            if (colors[i] != colors[n - 1]) ans = max(ans, n - 1 - i);
        }
        return ans;
    }
};
