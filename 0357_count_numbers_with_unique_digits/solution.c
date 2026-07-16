// LeetCode 0357 - Count Numbers with Unique Digits
// https://leetcode.com/problems/count-numbers-with-unique-digits/

int countNumbersWithUniqueDigits(int n) {
    if (n == 0) {
        return 1;
    }

    int total = 10;
    int unique = 9;
    int available = 9;

    for (int length = 2; length <= n; length++) {
        unique *= available;
        available -= 1;
        total += unique;
    }

    return total;
}
