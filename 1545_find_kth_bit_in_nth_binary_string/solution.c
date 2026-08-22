// LeetCode 1545 - Find Kth Bit in Nth Binary String
// https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

char findKthBit(int n, int k) {
    int invert = 0;
    int length = (1 << n) - 1;
    while (k != 1) {
        int middle = length / 2 + 1;
        if (k == middle) return invert ? '0' : '1';
        if (k > middle) {
            k = length - k + 1;
            invert ^= 1;
        }
        length /= 2;
    }
    return invert ? '1' : '0';
}
