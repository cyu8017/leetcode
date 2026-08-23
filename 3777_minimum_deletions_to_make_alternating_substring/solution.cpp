// LeetCode 3777 - Minimum Deletions To Make Alternating Substring
// https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/

#include <string>
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
    std::vector<int> minDeletions(std::string s, std::vector<std::vector<int>>& queries) {
        int n = (int)s.size();
        std::vector<int> nums(n, 0);
        BIT bit(n);
        for (int i = 1; i < n; i++) {
            if (s[i] == s[i - 1]) {
                nums[i] = 1;
                bit.update(i + 1, 1);
            }
        }
        std::vector<int> ans;
        for (auto& q : queries) {
            if (q[0] == 1) {
                int j = q[1];
                int delta = (nums[j] ^ 1) - nums[j];
                nums[j] ^= 1;
                bit.update(j + 1, delta);
                if (j + 1 < n) {
                    delta = (nums[j + 1] ^ 1) - nums[j + 1];
                    nums[j + 1] ^= 1;
                    bit.update(j + 2, delta);
                }
            } else {
                int l = q[1], r = q[2];
                ans.push_back(bit.query(r + 1) - bit.query(l + 1));
            }
        }
        return ans;
    }
};
