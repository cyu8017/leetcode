// LeetCode 1995 - Count Special Quadruplets
// https://leetcode.com/problems/count-special-quadruplets/

int countQuadruplets(int* nums, int numsSize) {
    int ans = 0;
    for (int a = 0; a < numsSize; a++) {
        for (int b = a + 1; b < numsSize; b++) {
            for (int c = b + 1; c < numsSize; c++) {
                for (int d = c + 1; d < numsSize; d++) {
                    if (nums[a] + nums[b] + nums[c] == nums[d]) ans++;
                }
            }
        }
    }
    return ans;
}
