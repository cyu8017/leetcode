// LeetCode 0926 - Flip String to Monotone Increasing
// https://leetcode.com/problems/flip-string-to-monotone-increasing/

int minFlipsMonoIncr(char* s) {
    int ones = 0, ans = 0;
    for (; *s; s++) {
        if (*s == '1') ones++;
        else ans = (ans + 1 < ones) ? ans + 1 : ones;
    }
    return ans;
}
