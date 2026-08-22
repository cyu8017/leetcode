// LeetCode 3536 - Maximum Product of Two Digits
// https://leetcode.com/problems/maximum-product-of-two-digits/

int maxProduct(int n) {
    int d[10], c = 0;
    if (n == 0) return 0;
    while (n > 0) { d[c++] = n % 10; n /= 10; }
    int a = 0, b = 0;
    for (int i = 0; i < c; i++) {
        if (d[i] >= a) { b = a; a = d[i]; }
        else if (d[i] > b) b = d[i];
    }
    return a * b;
}
