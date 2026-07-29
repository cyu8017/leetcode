// LeetCode 1998 - GCD Sort of an Array
#include <algorithm>
#include <cmath>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool gcdSort(std::vector<int>& nums) {
        int m = *std::max_element(nums.begin(), nums.end());
        std::vector<int> parent(m + 1);
        for (int i = 0; i <= m; i++) parent[i] = i;
        auto find = [&](int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        };
        auto unite = [&](int a, int b) {
            int ra = find(a), rb = find(b);
            if (ra != rb) parent[rb] = ra;
        };
        std::vector<int> spf(m + 1);
        for (int i = 0; i <= m; i++) spf[i] = i;
        for (int i = 2; i * i <= m; i++) {
            if (spf[i] == i) {
                for (int j = i * i; j <= m; j += i) if (spf[j] == j) spf[j] = i;
            }
        }
        std::unordered_set<int> uniq(nums.begin(), nums.end());
        for (int x : uniq) {
            int y = x;
            while (y > 1) {
                int p = spf[y];
                unite(x, p);
                while (y % p == 0) y /= p;
            }
        }
        std::vector<int> sorted = nums;
        std::sort(sorted.begin(), sorted.end());
        for (int i = 0; i < (int)nums.size(); i++) {
            if (find(nums[i]) != find(sorted[i])) return false;
        }
        return true;
    }
};
