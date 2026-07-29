// LeetCode 1963 - Minimum Number of Swaps to Make the String Balanced
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

int minSwaps(char* s) {
    int bal = 0, mx = 0;
    for (char* p = s; *p; p++) {
        if (*p == ']') bal++;
        else bal--;
        if (bal > mx) mx = bal;
    }
    return (mx + 1) / 2;
}
