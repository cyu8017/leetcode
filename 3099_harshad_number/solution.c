// LeetCode 3099 - Harshad Number
// https://leetcode.com/problems/harshad-number/

int sumOfTheDigitsOfHarshadNumber(int x) {
    int s = 0;
    for (int y = x; y > 0; y /= 10) s += y % 10;
    if (x % s == 0) return s;
    return -1;
}
