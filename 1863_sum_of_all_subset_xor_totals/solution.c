// LeetCode 1863 - Sum of All Subset XOR Totals
// https://leetcode.com/problems/sum-of-all-subset-xor-totals/

int subsetXORSum(int* nums, int numsSize) {
    int bits = 0;
    for (int i = 0; i < numsSize; i++) bits |= nums[i];
    int total = 0;
    for (int bit = 1; bit <= bits; bit <<= 1) {
        if (bits & bit) total += bit;
    }
    return total << (numsSize - 1);
}
