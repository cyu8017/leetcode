// LeetCode 2115 - Find All Possible Recipes from Given Supplies
// https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

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
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
        unordered_set<string> have(supplies.begin(), supplies.end());
        unordered_map<string, int> indeg;
        unordered_map<string, vector<string>> graph;
        for (int i = 0; i < (int)recipes.size(); i++) {
            indeg[recipes[i]] = ingredients[i].size();
            for (auto& ing : ingredients[i]) graph[ing].push_back(recipes[i]);
        }
        queue<string> q;
        for (auto& s : have) q.push(s);
        vector<string> ans;
        while (!q.empty()) {
            string cur = q.front(); q.pop();
            for (auto& nxt : graph[cur]) {
                if (--indeg[nxt] == 0) {
                    ans.push_back(nxt);
                    q.push(nxt);
                }
            }
        }
        return ans;
    }
};
