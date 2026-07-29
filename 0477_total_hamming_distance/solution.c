// LeetCode 0477 - Total Hamming Distance
// https://leetcode.com/problems/total-hamming-distance/

int totalHammingDistance(int* nums, int numsSize) {
    int total = 0;
    for (int bit = 0; bit < 32; bit++) {
        int ones = 0;
        for (int i = 0; i < numsSize; i++) {
            if (nums[i] & (1 << bit)) {
                ones++;
            }
        }
        total += ones * (numsSize - ones);
    }
    return total;
}
