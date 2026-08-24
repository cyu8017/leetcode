// LeetCode 2451 - Odd String Difference
// https://leetcode.com/problems/odd-string-difference/

export function oddString(words: string[]): string {
    const diff = (w) => {
        let b = '';
        for (let i = 1; i < w.length; i++) {
            const d = w.charCodeAt(i) - w.charCodeAt(i - 1);
            b += String.fromCharCode(d + 128) + ',';
        }
        return b;
    };
    const d0 = diff(words[0]), d1 = diff(words[1]);
    if (d0 === d1) {
        for (let i = 2; i < words.length; i++) {
            if (diff(words[i]) !== d0) return words[i];
        }
    }
    if (diff(words[2]) === d0) return words[1];
    return words[0];
}
