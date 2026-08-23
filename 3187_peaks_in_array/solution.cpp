// LeetCode 3187 - Peaks in Array
// https://leetcode.com/problems/peaks-in-array/

#include <vector>

class Solution {
    struct BIT {
        int n;
        std::vector<int> c;
        BIT(int n) : n(n), c(n + 1) {}
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
    std::vector<int> countOfPeaks(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        BIT tree(n - 1);
        auto update = [&](int i, int val) {
            if (i <= 0 || i >= n - 1) return;
            if (nums[i - 1] < nums[i] && nums[i] > nums[i + 1]) tree.update(i, val);
        };
        for (int i = 1; i < n - 1; i++) update(i, 1);
        std::vector<int> ans;
        for (auto& q : queries) {
            if (q[0] == 1) {
                int l = q[1] + 1, r = q[2] - 1, t = 0;
                if (l <= r) t = tree.query(r) - tree.query(l - 1);
                ans.push_back(t);
            } else {
                int idx = q[1], val = q[2];
                for (int i = idx - 1; i <= idx + 1; i++) update(i, -1);
                nums[idx] = val;
                for (int i = idx - 1; i <= idx + 1; i++) update(i, 1);
            }
        }
        return ans;
    }
};
