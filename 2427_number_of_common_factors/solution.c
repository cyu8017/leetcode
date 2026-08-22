// LeetCode 2427 - Number of Common Factors
// https://leetcode.com/problems/number-of-common-factors/

int commonFactors(int a, int b) {
    int g = a;
    while (b) { int t = g % b; g = b; b = t; }
    int ans = 0;
    for (int i = 1; i * i <= g; i++) {
        if (g % i == 0) {
            ans++;
            if (i * i != g) ans++;
        }
    }
    return ans;
}
