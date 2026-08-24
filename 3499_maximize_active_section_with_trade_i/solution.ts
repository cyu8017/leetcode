// LeetCode 3499 - Maximize Active Section with Trade I
// https://leetcode.com/problems/maximize-active-section-with-trade-i/

export function maxActiveSectionsAfterTrade(s: any): any {
    let ones = 0;
    for (const c of s) if (c === "1") ones++;
    const zeros = [];
    const n = s.length;
    for (let i = 0; i < n; ) {
        if (s[i] !== "0") { i++; continue; }
        let j = i;
        while (j < n && s[j] === "0") j++;
        zeros.push([i, j - 1]);
        i = j;
    }
    let best = 0;
    for (let i = 0; i + 1 < zeros.length; i++) {
        const gain = (zeros[i][1] - zeros[i][0] + 1) + (zeros[i + 1][1] - zeros[i + 1][0] + 1);
        if (gain > best) best = gain;
    }
    return ones + best;
}
