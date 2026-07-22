// LeetCode 1611 - Minimum One Bit Operations to Make Integers Zero
// https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

int minimumOneBitOperations(int n) {
    int ans = 0;
    while (n) {
        ans ^= n;
        n >>= 1;
    }
    return ans;
}
