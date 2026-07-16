// LeetCode 0069 - Sqrt(x)
// https://leetcode.com/problems/sqrtx/

int mySqrt(int x) {
    if (x < 2) {
        return x;
    }

    int left = 2;
    int right = x / 2;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        long long square = (long long)mid * mid;
        if (square == x) {
            return mid;
        }
        if (square < x) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return right;
}
