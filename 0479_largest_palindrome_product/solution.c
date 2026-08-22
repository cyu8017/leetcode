// LeetCode 0479 - Largest Palindrome Product
// https://leetcode.com/problems/largest-palindrome-product/

long long buildPalindrome(int first, int n) {
    long long result = first;
    int temp = first;
    if (n % 2 == 1) {
        temp /= 10;
    }
    // For this problem n digits mirrored: always even-length palindrome from n-digit first
    (void)n;
    temp = first;
    while (temp > 0) {
        result = result * 10 + temp % 10;
        temp /= 10;
    }
    return result;
}

int largestPalindrome(int n) {
    if (n == 1) {
        return 9;
    }
    int upper = 1;
    for (int i = 0; i < n; i++) {
        upper *= 10;
    }
    upper -= 1;
    int lower = 1;
    for (int i = 0; i < n - 1; i++) {
        lower *= 10;
    }

    for (int first = upper; first >= lower; first--) {
        long long candidate = buildPalindrome(first, n);
        for (int factor = upper; (long long)factor * factor >= candidate; factor--) {
            if (candidate % factor == 0) {
                long long other = candidate / factor;
                if (other >= lower && other <= upper) {
                    return (int)(candidate % 1337);
                }
            }
        }
    }
    return 0;
}
