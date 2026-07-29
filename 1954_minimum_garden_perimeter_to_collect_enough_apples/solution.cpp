// LeetCode 1954 - Minimum Garden Perimeter to Collect Enough Apples
class Solution {
public:
    long long minimumPerimeter(long long neededApples) {
        long long lo = 1, hi = 100000;
        while (lo < hi) {
            long long mid = (lo + hi) / 2;
            long long apples = 2 * mid * (mid + 1) * (2 * mid + 1);
            if (apples >= neededApples) hi = mid;
            else lo = mid + 1;
        }
        return 8 * lo;
    }
};
