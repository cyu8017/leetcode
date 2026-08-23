// LeetCode 3739 - Count Subarrays With Majority Element II
// https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

#include <vector>

class Solution {
    struct BIT {
        int n;
        std::vector<int> c;
        explicit BIT(int n_) : n(n_), c(n_ + 1, 0) {}
        void update(int x, int delta) {
            for (; x <= n; x += x & -x) c[x] += delta;
        }
        int query(int x) {
            int s = 0;
            for (; x > 0; x -= x & -x) s += c[x];
            return s;
        }
    };

public:
    long long countMajoritySubarrays(std::vector<int>& nums, int target) {
        int n = (int)nums.size();
        BIT tree(2 * n + 1);
        int s = n + 1;
        tree.update(s, 1);
        long long ans = 0;
        for (int x : nums) {
            if (x == target) s++;
            else s--;
            ans += tree.query(s - 1);
            tree.update(s, 1);
        }
        return ans;
    }
};
