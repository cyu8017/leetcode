// LeetCode 3378 - Count Connected Components in LCM Graph
// https://leetcode.com/problems/count-connected-components-in-lcm-graph/

#include <numeric>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
    static int gcd(int a, int b) {
        while (b) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

public:
    int countComponents(std::vector<int>& nums, int threshold) {
        int n = (int)nums.size();
        std::vector<int> parent(n);
        for (int i = 0; i < n; i++) parent[i] = i;
        auto find = [&](auto&& self, int x) -> int {
            if (parent[x] != x) parent[x] = self(self, parent[x]);
            return parent[x];
        };
        auto unite = [&](int a, int b) {
            int ra = find(find, a), rb = find(find, b);
            if (ra != rb) parent[ra] = rb;
        };
        std::unordered_map<int, int> idx;
        for (int i = 0; i < n; i++) idx[nums[i]] = i;
        for (int d = 1; d <= threshold; d++) {
            int first = -1;
            for (int m = d; m <= threshold; m += d) {
                auto it = idx.find(m);
                if (it != idx.end()) {
                    int i = it->second;
                    if (first == -1) first = i;
                    else if ((long long)nums[first] * nums[i] / gcd(nums[first], nums[i]) <= threshold)
                        unite(first, i);
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int a = nums[i], b = nums[j];
                int g = gcd(a, b);
                if ((long long)a / g * b <= threshold) unite(i, j);
            }
        }
        std::unordered_set<int> comp;
        for (int i = 0; i < n; i++) comp.insert(find(find, i));
        return (int)comp.size();
    }
};
