// LeetCode 2158 - Amount of New Area Painted Each Day
// https://leetcode.com/problems/amount-of-new-area-painted-each-day/

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
    vector<int> amountPainted(vector<vector<int>>& paint) {
        vector<int> ans(paint.size()), line(50001);
        for (int i = 0; i < (int)paint.size(); i++) {
            int start = paint[i][0], end = paint[i][1], j = start;
            while (j < end) {
                if (line[j] == 0) {
                    ans[i]++;
                    line[j] = end;
                    j++;
                } else {
                    int next = line[j];
                    line[j] = max(end, next);
                    j = next;
                }
            }
        }
        return ans;
    }
};
