// LeetCode 0476 - Number Complement
// https://leetcode.com/problems/number-complement/

int findComplement(int num) {
    unsigned int mask = (unsigned int)num;
    mask |= mask >> 1;
    mask |= mask >> 2;
    mask |= mask >> 4;
    mask |= mask >> 8;
    mask |= mask >> 16;
    return (int)((unsigned int)num ^ mask);
}
