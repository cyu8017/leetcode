// LeetCode 0186 - Reverse Words in a String II
// https://leetcode.com/problems/reverse-words-in-a-string-ii/

static void reverse(char* s, int left, int right) {
    while (left < right) {
        char temp = s[left];
        s[left++] = s[right];
        s[right--] = temp;
    }
}

void reverseWords(char* s, int sSize) {
    reverse(s, 0, sSize - 1);
    int start = 0;
    for (int end = 0; end <= sSize; ++end) {
        if (end == sSize || s[end] == ' ') {
            reverse(s, start, end - 1);
            start = end + 1;
        }
    }
}