// LeetCode 3134 - Find the Median of the Uniqueness Array
// https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

#include <vector>
#include <unordered_map>

class Solution {
public:
    int medianOfUniquenessArray(std::vector<int>& nums) {
        int n = (int)nums.size();
        long long m = (1LL + n) * n / 2;
        auto check = [&](int mx) {
            std::unordered_map<int, int> cnt;
            int l = 0;
            long long k = 0;
            for (int r = 0; r < n; r++) {
                cnt[nums[r]]++;
                while ((int)cnt.size() > mx) {
                    int y = nums[l++];
                    if (--cnt[y] == 0) cnt.erase(y);
                }
                k += r - l + 1;
                if (k >= (m + 1) / 2) return true;
            }
            return false;
        };
        int lo = 1, hi = n;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (check(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
