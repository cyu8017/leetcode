// LeetCode 0443 - String Compression
// https://leetcode.com/problems/string-compression/

export class Solution {
    compress(chars: string[]): number {
        let write = 0;
        let read = 0;
        while (read < chars.length) {
            const char = chars[read];
            let count = 0;
            while (read < chars.length && chars[read] === char) {
                read += 1;
                count += 1;
            }
            chars[write] = char;
            write += 1;
            if (count > 1) {
                for (const digit of String(count)) {
                    chars[write] = digit;
                    write += 1;
                }
            }
        }
        return write;
    }
}
