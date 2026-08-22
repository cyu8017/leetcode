// LeetCode 3513 - Number of Unique XOR Triplets I
// https://leetcode.com/problems/number-of-unique-xor-triplets-i/

int uniqueXorTriplets(int* nums, int numsSize) {
    (void)nums;
    int n = numsSize;
    if (n <= 2) return n;
    int len = 0;
    unsigned v = (unsigned)n;
    while (v) { len++; v >>= 1; }
    return 1 << len;
}
