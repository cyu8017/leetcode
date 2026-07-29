// LeetCode 0443 - String Compression
// https://leetcode.com/problems/string-compression/

int compress(char* chars, int charsSize) {
    int write = 0;
    int read = 0;
    while (read < charsSize) {
        char ch = chars[read];
        int count = 0;
        while (read < charsSize && chars[read] == ch) {
            read++;
            count++;
        }
        chars[write++] = ch;
        if (count > 1) {
            char buf[12];
            int len = 0;
            int temp = count;
            while (temp > 0) {
                buf[len++] = (char)('0' + temp % 10);
                temp /= 10;
            }
            for (int i = len - 1; i >= 0; i--) {
                chars[write++] = buf[i];
            }
        }
    }
    return write;
}
