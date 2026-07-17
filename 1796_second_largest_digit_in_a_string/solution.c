// LeetCode 1796 - Second Largest Digit in a String
// https://leetcode.com/problems/second-largest-digit-in-a-string/

int secondHighest(char* s) {
    int largest = -1;
    int second = -1;
    for (int i = 0; s[i] != '\0'; i++) {
        char ch = s[i];
        if (ch >= '0' && ch <= '9') {
            int d = ch - '0';
            if (d > largest) {
                second = largest;
                largest = d;
            } else if (d < largest && d > second) {
                second = d;
            }
        }
    }
    return second;
}
