// LeetCode 3064 - Guess the Number Using Bitwise Questions I
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/

/* Definition of commonSetBits API (provided by judge). */
int commonSetBits(int num);

int findNumber(void) {
    int n = 0;
    for (int i = 0; i < 32; i++) {
        if (commonSetBits(1 << i) > 0) n |= 1 << i;
    }
    return n;
}
