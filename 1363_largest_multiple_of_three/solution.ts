// LeetCode 1363 - Largest Multiple Of Three
// https://leetcode.com/problems/largest-multiple-of-three/

function largestMultipleOfThree(digits: number[]): string {
    const cnt = Array(10).fill(0);
    let rem = 0;
    for (const d of digits) {
        cnt[d]++;
        rem += d;
    }
    rem %= 3;
    const remove = (r: any, k: any): any => {
        for (let d = r; d < 10; d += 3) {
            while (cnt[d] && k) {
                cnt[d]--;
                k--;
            }
            if (!k) return true;
        }
        return false;
    };
    if (rem && !remove(rem, 1)) remove(3 - rem, 2);
    let s = "";
    for (let d = 9; d >= 0; d--) s += String(d).repeat(cnt[d]);
    return s && s[0] === "0" ? "0" : s;
}
