// LeetCode 2748 - Number of Beautiful Pairs
// https://leetcode.com/problems/number-of-beautiful-pairs/

static int gcd2748(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}

static int firstDigit2748(int x) {
    while (x >= 10) x /= 10;
    return x;
}

int countBeautifulPairs(int* nums, int numsSize) {
    int ans = 0;
    int freq[10] = {0};
    for (int i = 0; i < numsSize; i++) {
        int last = nums[i] % 10;
        for (int d = 1; d <= 9; d++)
            if (freq[d] > 0 && gcd2748(d, last) == 1) ans += freq[d];
        freq[firstDigit2748(nums[i])]++;
    }
    return ans;
}
