// LeetCode 1529 - Minimum Suffix Flips
// https://leetcode.com/problems/minimum-suffix-flips/

int minFlips(char* target) {
    int ans = 0;
    char prev = '0';
    for (; *target; target++) {
        if (*target != prev) {
            ans++;
            prev = *target;
        }
    }
    return ans;
}
