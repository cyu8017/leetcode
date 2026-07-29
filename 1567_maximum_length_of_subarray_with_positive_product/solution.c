// LeetCode 1567 - Maximum Length of Subarray With Positive Product
// https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

int getMaxLen(int* nums, int numsSize) {
    int positive = 0, negative = 0, answer = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        if (x == 0) {
            positive = negative = 0;
        } else if (x > 0) {
            positive += 1;
            negative = negative ? negative + 1 : 0;
        } else {
            int np = negative ? negative + 1 : 0;
            int nn = positive + 1;
            positive = np;
            negative = nn;
        }
        if (positive > answer) answer = positive;
    }
    return answer;
}
