// LeetCode 1017 - Convert to Base -2
// https://leetcode.com/problems/convert-to-base-2/

function baseNeg2(n: number): string {
    if (n === 0) return '0';
    const ans = [];
    while (n !== 0) {
        let rem = n % -2;
        n = Math.trunc(n / -2);
        if (rem < 0) {
            n += 1;
            rem += 2;
        }
        ans.push(String(rem));
    }
    return ans.reverse().join('');
}
