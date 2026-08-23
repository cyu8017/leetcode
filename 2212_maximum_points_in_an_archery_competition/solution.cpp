// LeetCode 2212 - Maximum Points in an Archery Competition
// https://leetcode.com/problems/maximum-points-in-an-archery-competition/

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
    vector<int> maximumBobPoints(int numArrows, vector<int>& aliceArrows) {
        int bestScore = -1;
        vector<int> best(12);
        function<void(int,int,int,vector<int>&)> dfs = [&](int i, int remain, int score, vector<int>& bob) {
            if (i == 12) {
                if (score > bestScore) {
                    bestScore = score;
                    best = bob;
                    if (remain > 0) best[0] += remain;
                }
                return;
            }
            dfs(i + 1, remain, score, bob);
            int need = aliceArrows[i] + 1;
            if (remain >= need) {
                bob[i] = need;
                dfs(i + 1, remain - need, score + i, bob);
                bob[i] = 0;
            }
        };
        vector<int> bob(12);
        dfs(0, numArrows, 0, bob);
        return best;
    }
};
