// LeetCode 3013 - Divide an Array Into Subarrays With Minimum Cost II
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

#include <algorithm>
#include <vector>

class Solution {
    struct BITI {
        int n;
        std::vector<int> c;
        explicit BITI(int n_) : n(n_), c(n_ + 1, 0) {}
        void upd(int x, int d) { for (; x <= n; x += x & -x) c[x] += d; }
        int qry(int x) { int s = 0; for (; x > 0; x -= x & -x) s += c[x]; return s; }
    };
    struct BITL {
        int n;
        std::vector<long long> c;
        explicit BITL(int n_) : n(n_), c(n_ + 1, 0) {}
        void upd(int x, long long d) { for (; x <= n; x += x & -x) c[x] += d; }
        long long qry(int x) { long long s = 0; for (; x > 0; x -= x & -x) s += c[x]; return s; }
    };
    static int kth(BITI& cnt, int m, int k) {
        int idx = 0;
        for (int bit = 1 << 20; bit; bit >>= 1) {
            int nidx = idx + bit;
            if (nidx <= m && cnt.c[nidx] < k) {
                k -= cnt.c[nidx];
                idx = nidx;
            }
        }
        return idx + 1;
    }
public:
    long long minimumCost(std::vector<int>& nums, int k, int dist) {
        k--;
        int n = (int)nums.size();
        std::vector<int> uniq = nums;
        std::sort(uniq.begin(), uniq.end());
        uniq.erase(std::unique(uniq.begin(), uniq.end()), uniq.end());
        int m = (int)uniq.size();
        BITI cnt(m + 2);
        BITL sum(m + 2);
        auto add_val = [&](int x, int d) {
            int r = (int)(std::lower_bound(uniq.begin(), uniq.end(), x) - uniq.begin()) + 1;
            cnt.upd(r, d);
            sum.upd(r, (long long)d * x);
        };
        auto sum_smallest = [&](int kk) -> long long {
            if (kk <= 0) return 0;
            int r = kth(cnt, m, kk);
            int before = cnt.qry(r - 1);
            long long s = sum.qry(r - 1);
            s += (long long)(kk - before) * uniq[r - 1];
            return s;
        };
        int end = std::min(dist + 1, n - 1);
        for (int i = 1; i <= end; i++) add_val(nums[i], 1);
        int kk = std::min(k, end);
        long long ans = nums[0] + sum_smallest(kk);
        for (int i = dist + 2; i < n; i++) {
            add_val(nums[i - dist - 1], -1);
            add_val(nums[i], 1);
            kk = std::min(k, dist + 1);
            ans = std::min(ans, nums[0] + sum_smallest(kk));
        }
        return ans;
    }
};
