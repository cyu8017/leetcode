// LeetCode 2717 - Semi-Ordered Permutation
// https://leetcode.com/problems/semi-ordered-permutation/

int semiOrderedPermutation(int* nums, int numsSize) {
    int pos1 = 0, posN = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 1) pos1 = i;
        if (nums[i] == numsSize) posN = i;
    }
    int ans = pos1 + (numsSize - 1 - posN);
    if (pos1 > posN) ans--;
    return ans;
}
