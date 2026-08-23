// LeetCode 2029 - Stone Game IX
// https://leetcode.com/problems/stone-game-ix/

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
    bool stoneGameIX(vector<int>& stones) {
        int cnt[3] = {};
        for (int s : stones) cnt[s % 3]++;
        if (cnt[0] % 2 == 0) return cnt[1] > 0 && cnt[2] > 0;
        return abs(cnt[1] - cnt[2]) > 2;
    }
};
