// LeetCode 2096 - Step-By-Step Directions From a Binary Tree Node to Another
// https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

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

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
    bool path(TreeNode* node, int target, string& p) {
        if (!node) return false;
        if (node->val == target) return true;
        p.push_back('L');
        if (path(node->left, target, p)) return true;
        p.back() = 'R';
        if (path(node->right, target, p)) return true;
        p.pop_back();
        return false;
    }
public:
    string getDirections(TreeNode* root, int startValue, int destValue) {
        string ps, pd;
        path(root, startValue, ps);
        path(root, destValue, pd);
        int i = 0;
        while (i < (int)ps.size() && i < (int)pd.size() && ps[i] == pd[i]) i++;
        return string(ps.size() - i, 'U') + pd.substr(i);
    }
};
