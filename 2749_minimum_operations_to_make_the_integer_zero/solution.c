// LeetCode 2749 - Minimum Operations to Make the Integer Zero
// https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

static int bitsCount2749(long long x) {
    int cnt = 0;
    while (x > 0) { cnt++; x &= x - 1; }
    return cnt;
}

int makeTheIntegerZero(int num1, int num2) {
    for (int ops = 1; ops <= 60; ops++) {
        long long remain = (long long)num1 - (long long)ops * num2;
        if (remain < ops) continue;
        if (bitsCount2749(remain) <= ops) return ops;
    }
    return -1;
}
