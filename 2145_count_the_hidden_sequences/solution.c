// LeetCode 2145 - Count the Hidden Sequences
// https://leetcode.com/problems/count-the-hidden-sequences/

int numberOfArrays(int* differences, int differencesSize, int lower, int upper) {
    long long cur = 0, mn = 0, mx = 0;
    for (int i = 0; i < differencesSize; i++) {
        cur += differences[i];
        if (cur < mn) mn = cur;
        if (cur > mx) mx = cur;
    }
    long long res = (long long)(upper - lower) - (mx - mn) + 1;
    return res < 0 ? 0 : (int)res;
}
