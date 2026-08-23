// LeetCode 2059 - Minimum Operations to Convert Number
// https://leetcode.com/problems/minimum-operations-to-convert-number/

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
    int minimumOperations(vector<int>& nums, int start, int goal) {
        if (start == goal) return 0;
        unordered_set<int> vis{start};
        queue<int> q;
        q.push(start);
        int steps = 0;
        while (!q.empty()) {
            steps++;
            int sz = (int)q.size();
            while (sz--) {
                int cur = q.front(); q.pop();
                for (int x : nums) {
                    for (int nxt : {cur + x, cur - x, cur ^ x}) {
                        if (nxt == goal) return steps;
                        if (nxt >= 0 && nxt <= 1000 && !vis.count(nxt)) {
                            vis.insert(nxt);
                            q.push(nxt);
                        }
                    }
                }
            }
        }
        return -1;
    }
};
