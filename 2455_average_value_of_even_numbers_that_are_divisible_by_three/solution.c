// LeetCode 2455 - Average Value of Even Numbers That Are Divisible by Three
// https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

int averageValue(int* nums, int numsSize) {
    int sum = 0, cnt = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] % 6 == 0) {
            sum += nums[i];
            cnt++;
        }
    }
    return cnt == 0 ? 0 : sum / cnt;
}
