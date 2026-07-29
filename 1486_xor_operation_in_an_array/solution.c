// LeetCode 1486 - XOR Operation in an Array
// https://leetcode.com/problems/xor-operation-in-an-array/

int xorOperation(int n, int start) {
    int ans = 0;
    for (int i = 0; i < n; i++) ans ^= start + 2 * i;
    return ans;
}
