// LeetCode 1513 - Number of Substrings With Only 1s
// https://leetcode.com/problems/number-of-substrings-with-only-1s/

int numSub(char* s) {
    long long ans = 0, run = 0;
    for (; *s; s++) {
        if (*s == '1') {
            run++;
            ans += run;
        } else {
            run = 0;
        }
    }
    return (int)(ans % 1000000007LL);
}
