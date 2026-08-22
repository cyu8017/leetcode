// LeetCode 0389 - Find the Difference
// https://leetcode.com/problems/find-the-difference/

char findTheDifference(char* s, char* t) {
    int xorValue = 0;

    for (int index = 0; s[index] != '\0'; index++) {
        xorValue ^= s[index];
    }
    for (int index = 0; t[index] != '\0'; index++) {
        xorValue ^= t[index];
    }

    return (char)xorValue;
}
