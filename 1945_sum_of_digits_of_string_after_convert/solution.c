// LeetCode 1945 - Sum of Digits of String After Convert
// https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

int getLucky(char* s, int k) {
    int sum = 0;
    for (char* p = s; *p; p++) {
        int v = *p - 'a' + 1;
        sum += v / 10 + v % 10;
    }
    for (int i = 1; i < k; i++) {
        int next = 0;
        while (sum > 0) {
            next += sum % 10;
            sum /= 10;
        }
        sum = next;
    }
    return sum;
}
