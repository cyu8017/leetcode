// LeetCode 3954 - Sum Of Compatible Numbers In Range I
// https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/

int sumOfGoodIntegers(int n, int k) {
    int start = 1 > n - k ? 1 : n - k;
    int end = n + k;
    int ans = 0;
    for (int x = start; x <= end; x++) if ((n & x) == 0) ans += x;
    return ans;
}
