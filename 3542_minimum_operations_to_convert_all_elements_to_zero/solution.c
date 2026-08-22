// LeetCode 3542 - Minimum Operations to Convert All Elements to Zero
// https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

int minOperations(int* nums, int numsSize) {
    int stk[100005];
    int top = 0, ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        while (top > 0 && stk[top - 1] > x) {
            ans++;
            top--;
        }
        if (x != 0 && (top == 0 || stk[top - 1] != x)) {
            stk[top++] = x;
        }
    }
    ans += top;
    return ans;
}
