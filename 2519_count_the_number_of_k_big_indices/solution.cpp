// LeetCode 2519 - Count the Number of K-Big Indices
// https://leetcode.com/problems/count-the-number-of-k-big-indices/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
    struct Fenwick {
        std::vector<int> bit;
        Fenwick(int n) : bit(n + 2) {}
        void add(int i, int v) {
            for (; i < (int)bit.size(); i += i & -i) bit[i] += v;
        }
        int sum(int i) {
            int s = 0;
            for (; i > 0; i -= i & -i) s += bit[i];
            return s;
        }
    };
public:
    int kBigIndices(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> uniq = nums;
        std::sort(uniq.begin(), uniq.end());
        uniq.erase(std::unique(uniq.begin(), uniq.end()), uniq.end());
        std::unordered_map<int, int> rank;
        for (int i = 0; i < (int)uniq.size(); i++) rank[uniq[i]] = i + 1;
        int m = (int)uniq.size();
        std::vector<int> left(n), right(n);
        Fenwick ft(m);
        for (int i = 0; i < n; i++) {
            int r = rank[nums[i]];
            left[i] = ft.sum(r - 1);
            ft.add(r, 1);
        }
        ft = Fenwick(m);
        for (int i = n - 1; i >= 0; i--) {
            int r = rank[nums[i]];
            right[i] = ft.sum(r - 1);
            ft.add(r, 1);
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (left[i] >= k && right[i] >= k) ans++;
        }
        return ans;
    }
};
