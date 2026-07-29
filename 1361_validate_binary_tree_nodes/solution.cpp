#include <unordered_set>
#include <vector>

class Solution {
public:
    bool validateBinaryTreeNodes(int n, std::vector<int>& leftChild, std::vector<int>& rightChild) {
        std::vector<int> indeg(n, 0);
        for (int x : leftChild) {
            if (x != -1) {
                if (++indeg[x] > 1) return false;
            }
        }
        for (int x : rightChild) {
            if (x != -1) {
                if (++indeg[x] > 1) return false;
            }
        }
        std::vector<int> roots;
        for (int i = 0; i < n; ++i) if (indeg[i] == 0) roots.push_back(i);
        if (roots.size() != 1) return false;
        std::unordered_set<int> seen;
        std::vector<int> st = roots;
        while (!st.empty()) {
            int u = st.back(); st.pop_back();
            if (seen.count(u)) return false;
            seen.insert(u);
            if (leftChild[u] != -1) st.push_back(leftChild[u]);
            if (rightChild[u] != -1) st.push_back(rightChild[u]);
        }
        return (int)seen.size() == n;
    }
};
