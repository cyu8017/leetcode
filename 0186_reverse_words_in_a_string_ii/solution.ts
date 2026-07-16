// LeetCode 0186 - Reverse Words in a String II
// https://leetcode.com/problems/reverse-words-in-a-string-ii/

export function reverseWords(s: string[]): void {
    const reverse = (left: number, right: number): void => {
        while (left < right) {
            [s[left], s[right]] = [s[right], s[left]];
            left++;
            right--;
        }
    };

    reverse(0, s.length - 1);
    let start = 0;
    for (let end = 0; end <= s.length; end++) {
        if (end === s.length || s[end] === " ") {
            reverse(start, end - 1);
            start = end + 1;
        }
    }
}