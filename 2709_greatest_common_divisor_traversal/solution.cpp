// LeetCode 2709 - Greatest Common Divisor Traversal
// https://leetcode.com/problems/greatest-common-divisor-traversal/

#include <vector>
#include <functional>
#include <algorithm>

class Solution {
public:
    bool canTraverseAllPairs(std::vector<int>& nums) {
        int n = (int)nums.size();
        if (n == 1) return true;
        int mx = *std::max_element(nums.begin(), nums.end());
        std::vector<int> parent(mx + 1);
        for (int i = 0; i <= mx; i++) parent[i] = i;
        std::function<int(int)> find = [&](int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        };
        auto unite = [&](int a, int b) {
            int ra = find(a), rb = find(b);
            if (ra != rb) parent[ra] = rb;
        };
        std::vector<char> has(mx + 1);
        for (int x : nums) {
            if (x == 1) return false;
            has[x] = 1;
        }
        std::vector<int> sieve(mx + 1);
        for (int i = 2; i <= mx; i++) {
            if (sieve[i] == 0) {
                for (int j = i; j <= mx; j += i) {
                    if (sieve[j] == 0) sieve[j] = i;
                    if (has[j]) unite(i, j);
                }
            }
        }
        int root = find(nums[0]);
        for (int x : nums) if (find(x) != root) return false;
        return true;
    }
};
