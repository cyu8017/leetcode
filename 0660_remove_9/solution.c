// LeetCode 0660 - Remove 9
// https://leetcode.com/problems/remove-9/

int newInteger(int n) {
    int result = 0;
    int base = 1;
    while (n) {
        result += (n % 9) * base;
        n /= 9;
        base *= 10;
    }
    return result;
}
