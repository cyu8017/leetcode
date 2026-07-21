// LeetCode 1837 - Sum of Digits in Base K
// https://leetcode.com/problems/sum-of-digits-in-base-k/

int sumBase(int n, int k) {
    int total = 0;
    while (n) {
        total += n % k;
        n /= k;
    }
    return total;
}
