// LeetCode 0371 - Sum of Two Integers
// https://leetcode.com/problems/sum-of-two-integers/

int getSum(int a, int b) {
    unsigned int mask = 0xFFFFFFFFu;
    unsigned int ua = (unsigned int)a;
    unsigned int ub = (unsigned int)b;

    while (ub) {
        unsigned int carry = (ua & ub) << 1;
        ua = (ua ^ ub) & mask;
        ub = carry & mask;
    }

    if (ua <= 0x7FFFFFFFu) {
        return (int)ua;
    }
    return (int)(~(ua ^ mask));
}
