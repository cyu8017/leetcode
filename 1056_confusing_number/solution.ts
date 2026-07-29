// LeetCode 1056 - Confusing Number
// https://leetcode.com/problems/confusing-number/

function confusingNumber(n: number): boolean {
    const rotate: Record<string, string> = { "0": "0", "1": "1", "6": "9", "8": "8", "9": "6" };
    const s = String(n);
    let rotated = "";
    for (let i = s.length - 1; i >= 0; i--) {
        const ch = s[i];
        if (!(ch in rotate)) return false;
        rotated += rotate[ch];
    }
    return rotated !== s;
}
