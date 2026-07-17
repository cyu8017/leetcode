// LeetCode 1782 - Count Pairs Of Nodes
// https://leetcode.com/problems/count-pairs-of-nodes/

#include <algorithm>
#include <unordered_map>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> countPairs(int n, std::vector<std::vector<int>>& edges, std::vector<int>& queries) {
        std::vector<int> deg(n + 1, 0);
        std::unordered_map<long long, int> shared;
        for (const auto& edge : edges) {
            int a = std::min(edge[0], edge[1]);
            int b = std::max(edge[0], edge[1]);
            deg[a]++;
            deg[b]++;
            shared[(long long)a * 100000 + b]++;
        }
        std::vector<int> sortedDeg(deg.begin() + 1, deg.end());
        std::sort(sortedDeg.begin(), sortedDeg.end());
        std::vector<int> ans;
        ans.reserve(queries.size());
        for (int q : queries) {
            int res = 0;
            int left = 0;
            int right = n - 1;
            while (left < right) {
                if (sortedDeg[left] + sortedDeg[right] > q) {
                    res += right - left;
                    right--;
                } else {
                    left++;
                }
            }
            for (const auto& [key, count] : shared) {
                int a = (int)(key / 100000);
                int b = (int)(key % 100000);
                int sum = deg[a] + deg[b];
                if (sum > q && q >= sum - count) {
                    res--;
                }
            }
            ans.push_back(res);
        }
        return ans;
    }
};
