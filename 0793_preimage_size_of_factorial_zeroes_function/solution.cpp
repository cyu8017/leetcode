// LeetCode 0793 - Preimage Size of Factorial Zeroes Function
// https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

class Solution {
public:
    int preimageSizeFZF(int k) {
        return zeros(firstGe(k)) == k ? 5 : 0;
    }

private:
    long long zeros(long long x) {
        long long count = 0;
        while (x) {
            x /= 5;
            count += x;
        }
        return count;
    }

    long long firstGe(long long target) {
        long long lo = 0;
        long long hi = 5LL * (target + 1);
        while (lo < hi) {
            long long mid = lo + (hi - lo) / 2;
            if (zeros(mid) < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
};
