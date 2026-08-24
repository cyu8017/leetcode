// LeetCode 2067 - Number of Equal Count Substrings
// https://leetcode.com/problems/number-of-equal-count-substrings/

export function equalCountSubstrings(s: string, count: number): number {
    let ans = 0;
    const n = s.length;
    const seen = new Array(26).fill(false);
    let maxUnique = 0;
    for (const c of s) {
        const i = c.charCodeAt(0) - 97;
        if (!seen[i]) { seen[i] = true; maxUnique++; }
    }
    for (let u = 1; u <= maxUnique; u++) {
        const needLen = u * count;
        if (needLen > n) break;
        const freq = new Array(26).fill(0);
        let have = 0;
        for (let i = 0; i < n; i++) {
            const c = s.charCodeAt(i) - 97;
            freq[c]++;
            if (freq[c] === count) have++;
            else if (freq[c] === count + 1) have--;
            if (i >= needLen) {
                const p = s.charCodeAt(i - needLen) - 97;
                if (freq[p] === count) have--;
                else if (freq[p] === count + 1) have++;
                freq[p]--;
            }
            if (i + 1 >= needLen && have === u) ans++;
        }
    }
    return ans;
}
