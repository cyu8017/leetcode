// LeetCode 0761 - Special Binary String
// https://leetcode.com/problems/special-binary-string/

export function makeLargestSpecial(s: string): string {
    const parts = [];
    let balance = 0, start = 0;
    for (let i = 0; i < s.length; i++) {
        balance += s[i] === '1' ? 1 : -1;
        if (balance === 0) {
            parts.push('1' + makeLargestSpecial(s.substring(start + 1, i)) + '0');
            start = i + 1;
        }
    }
    parts.sort((a, b) => (a < b ? 1 : a > b ? -1 : 0));
    return parts.join('');
}
