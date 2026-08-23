// LeetCode 0443 - String Compression
// https://leetcode.com/problems/string-compression/

public class Solution {
    public int Compress(char[] chars) {
        int write = 0;
        int read = 0;
        while (read < chars.Length) {
            char ch = chars[read];
            int count = 0;
            while (read < chars.Length && chars[read] == ch) {
                read++;
                count++;
            }
            chars[write++] = ch;
            if (count > 1) {
                foreach (char digit in count.ToString()) {
                    chars[write++] = digit;
                }
            }
        }
        return write;
    }
}
