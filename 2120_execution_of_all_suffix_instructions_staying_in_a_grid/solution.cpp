// LeetCode 2120 - Execution of All Suffix Instructions Staying in a Grid
// https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

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
    vector<int> executeInstructions(int n, vector<int>& startPos, string s) {
        int m = s.size();
        vector<int> ans(m);
        for (int i = 0; i < m; i++) {
            int r = startPos[0], c = startPos[1], cnt = 0;
            for (int j = i; j < m; j++) {
                if (s[j] == 'L') c--;
                else if (s[j] == 'R') c++;
                else if (s[j] == 'U') r--;
                else r++;
                if (r < 0 || r >= n || c < 0 || c >= n) break;
                cnt++;
            }
            ans[i] = cnt;
        }
        return ans;
    }
};
