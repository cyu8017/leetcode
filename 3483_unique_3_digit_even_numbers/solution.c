// LeetCode 3483 - Unique 3-Digit Even Numbers
// https://leetcode.com/problems/unique-3-digit-even-numbers/

int totalNumbers(int* digits, int digitsSize) {
    int seen[1000] = {0};
    int n = digitsSize;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (j == i) continue;
            for (int k = 0; k < n; k++) {
                if (k == i || k == j) continue;
                if (digits[i] == 0) continue;
                if (digits[k] % 2 != 0) continue;
                seen[digits[i] * 100 + digits[j] * 10 + digits[k]] = 1;
            }
        }
    }
    int cnt = 0;
    for (int i = 0; i < 1000; i++) cnt += seen[i];
    return cnt;
}
