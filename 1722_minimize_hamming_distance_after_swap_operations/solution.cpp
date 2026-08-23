// LeetCode 1722 - Minimize Hamming Distance After Swap Operations
// https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

#include <numeric>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minimumHammingDistance(std::vector<int>& source, std::vector<int>& target,
                               std::vector<std::vector<int>>& allowedSwaps) {
        int n = (int)source.size();
        parent.resize(n);
        std::iota(parent.begin(), parent.end(), 0);
        for (const auto& swap : allowedSwaps) {
            unite(swap[0], swap[1]);
        }
        std::unordered_map<int, std::unordered_map<int, int>> groups;
        for (int i = 0; i < n; i++) {
            groups[find(i)][source[i]]++;
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            auto& counts = groups[find(i)];
            auto it = counts.find(target[i]);
            if (it != counts.end() && it->second > 0) {
                it->second--;
            } else {
                ans++;
            }
        }
        return ans;
    }

private:
    std::vector<int> parent;

    int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    void unite(int a, int b) {
        int ra = find(a);
        int rb = find(b);
        if (ra != rb) {
            parent[rb] = ra;
        }
    }
};
