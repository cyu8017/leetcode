// LeetCode 2070 - Most Beautiful Item for Each Query
// https://leetcode.com/problems/most-beautiful-item-for-each-query/

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
    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
        sort(items.begin(), items.end());
        int maxB = 0;
        for (auto& it : items) {
            maxB = max(maxB, it[1]);
            it[1] = maxB;
        }
        vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int lo = 0, hi = (int)items.size();
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (items[mid][0] <= queries[i]) lo = mid + 1;
                else hi = mid;
            }
            ans[i] = lo == 0 ? 0 : items[lo - 1][1];
        }
        return ans;
    }
};
