// LeetCode 0261 - Graph Valid Tree
// https://leetcode.com/problems/graph-valid-tree/

#include <vector>
using namespace std;

class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if ((int)edges.size() != n - 1) {
            return false;
        }
        vector<int> parent(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        for (const auto& edge : edges) {
            int rootLeft = find(parent, edge[0]);
            int rootRight = find(parent, edge[1]);
            if (rootLeft == rootRight) {
                return false;
            }
            parent[rootLeft] = rootRight;
        }
        return true;
    }

private:
    int find(vector<int>& parent, int node) {
        if (parent[node] != node) {
            parent[node] = find(parent, parent[node]);
        }
        return parent[node];
    }
};
