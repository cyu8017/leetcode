// LeetCode 0258 - Add Digits
// https://leetcode.com/problems/add-digits/

int addDigits(int num) {
    if (num == 0) {
        return 0;
    }
    return 1 + (num - 1) % 9;
}
