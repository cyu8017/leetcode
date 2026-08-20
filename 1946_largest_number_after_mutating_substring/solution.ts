// LeetCode 1946 - Largest Number After Mutating Substring
// https://leetcode.com/problems/largest-number-after-mutating-substring/

function maximumNumber(num: string, change: number[]): string {
    const chars = num.split("");
    let started = false;
    for (let i = 0; i < chars.length; i++) {
        const d = chars[i].charCodeAt(0) - 48;
        const mapped = change[d];
        if (mapped > d) {
            chars[i] = String(mapped);
            started = true;
        } else if (mapped < d && started) break;
    }
    return chars.join("");
}
