// LeetCode 4013 - Count Subarrays With Even Odd Ratio II
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/

#include <algorithm>
#include <cstdint>
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
            int sum = 0;
            for (; x > 0; x -= x & -x) sum += c[x];
            return sum;
        }
    };

public:
    long long countRatioSubarrays(std::vector<int>& nums, int a, int b) {
        int n = (int)nums.size();
        std::vector<int64_t> s(n + 1, 0);
        for (int i = 0; i < n; i++) {
            if (nums[i] % 2 == 1) s[i + 1] = s[i] + (int64_t)a;
            else s[i + 1] = s[i] - (int64_t)b;
        }

        std::vector<int64_t> st = s;
        std::sort(st.begin(), st.end());
        st.erase(std::unique(st.begin(), st.end()), st.end());

        BIT bit((int)st.size() + 1);
        int64_t ans = 0;
        for (int64_t v : s) {
            int x = (int)(std::lower_bound(st.begin(), st.end(), v) - st.begin()) + 1;
            ans += (int64_t)bit.query(x);
            bit.update(x, 1);
        }
        return ans;
    }
};
