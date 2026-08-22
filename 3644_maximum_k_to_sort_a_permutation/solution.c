// LeetCode 3644 - Maximum K to Sort a Permutation
// https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

static int imax(int a,int b){return a>b?a:b;}
int sortPermutation(int* nums, int numsSize) {
    int ans = -1;
    for (int i = 0; i < numsSize; i++) if (i != nums[i]) ans &= nums[i];
    return imax(ans, 0);
}
