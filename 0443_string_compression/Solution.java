// LeetCode 0443 - String Compression
// https://leetcode.com/problems/string-compression/

class Solution {
    public int compress(char[] chars) {
        int write = 0;
        int read = 0;
        while (read < chars.length) {
            char ch = chars[read];
            int count = 0;
            while (read < chars.length && chars[read] == ch) {
                read++;
                count++;
            }
            chars[write++] = ch;
            if (count > 1) {
                for (char digit : String.valueOf(count).toCharArray()) {
                    chars[write++] = digit;
                }
            }
        }
        return write;
    }
}
