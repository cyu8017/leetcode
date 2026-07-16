// LeetCode 0374 - Guess Number Higher or Lower
// https://leetcode.com/problems/guess-number-higher-or-lower/

int guess(int num) {
    (void)num;
    return 0;
}

int guessNumber(int n) {
    int left = 1;
    int right = n;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        int result = guess(mid);
        if (result == 0) {
            return mid;
        }
        if (result < 0) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return left;
}
