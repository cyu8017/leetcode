// LeetCode 1894 - Find the Student that Will Replace the Chalk
// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

int chalkReplacer(int* chalk, int chalkSize, int k) {
    long long total = 0;
    for (int i = 0; i < chalkSize; i++) total += chalk[i];
    long long remain = k % total;
    for (int i = 0; i < chalkSize; i++) {
        if (remain < chalk[i]) return i;
        remain -= chalk[i];
    }
    return 0;
}
