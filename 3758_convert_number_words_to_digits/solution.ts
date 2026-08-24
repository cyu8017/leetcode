// LeetCode 3758 - Convert Number Words To Digits
// https://leetcode.com/problems/convert_number_words_to_digits/

export function convertNumber(s: any): any {
    const d = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    const n = s.length;
    let ans = '';
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < 10; j++) {
            const m = d[j].length;
            if (i + m <= n && s.substring(i, i + m) === d[j]) {
                ans += String.fromCharCode(48 + j);
                i += m - 1;
                break;
            }
        }
    }
    return ans;
}
