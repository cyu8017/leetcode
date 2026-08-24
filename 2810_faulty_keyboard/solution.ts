// LeetCode 2810 - Faulty Keyboard
// https://leetcode.com/problems/faulty-keyboard/

export function finalString(s: string): string {
    let b = '';
    for (const c of s) {
        if (c === 'i') b = b.split('').reverse().join('');
        else b += c;
    }
    return b;
}
