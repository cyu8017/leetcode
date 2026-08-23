// LeetCode 2003 - Smallest Missing Genetic Value in Each Subtree
// https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/

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
    vector<int> smallestMissingValueSubtree(vector<int>& parents, vector<int>& nums) {
        int n = (int)parents.size();
        vector<vector<int>> children(n);
        for (int i = 1; i < n; i++) children[parents[i]].push_back(i);
        vector<int> ans(n, 1);
        int one = -1;
        for (int i = 0; i < n; i++) if (nums[i] == 1) { one = i; break; }
        if (one < 0) return ans;
        unordered_set<int> seen;
        function<void(int)> collect = [&](int u) {
            if (seen.count(nums[u])) return;
            seen.insert(nums[u]);
            for (int v : children[u]) collect(v);
        };
        int miss = 1, node = one, prev = -1;
        while (node != -1) {
            for (int v : children[node]) if (v != prev) collect(v);
            seen.insert(nums[node]);
            while (seen.count(miss)) miss++;
            ans[node] = miss;
            prev = node;
            node = parents[node];
        }
        return ans;
    }
};
