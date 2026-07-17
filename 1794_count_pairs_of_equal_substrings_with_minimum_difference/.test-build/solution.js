"use strict";
// LeetCode 1794 - Count Pairs of Equal Substrings With Minimum Difference
// https://leetcode.com/problems/count-pairs-of-equal-substrings-with-minimum-difference/
function countQuadruples(firstString, secondString) {
    const first = new Map();
    const lastF = new Map();
    const lastS = new Map();
    for (let i = 0; i < firstString.length; i++) {
        const ch = firstString[i];
        if (!first.has(ch))
            first.set(ch, i);
        lastF.set(ch, i);
    }
    for (let i = 0; i < secondString.length; i++) {
        lastS.set(secondString[i], i);
    }
    let best = Infinity;
    for (const ch of first.keys()) {
        if (lastS.has(ch)) {
            best = Math.min(best, lastF.get(ch) - lastS.get(ch));
        }
    }
    if (best === Infinity)
        return 0;
    let ans = 0;
    for (const ch of first.keys()) {
        if (!lastS.has(ch) || lastF.get(ch) - lastS.get(ch) !== best)
            continue;
        let iCount = 0;
        for (let k = first.get(ch); k <= lastF.get(ch); k++) {
            if (firstString[k] === ch)
                iCount++;
        }
        let aCount = 0;
        for (let k = 0; k <= lastS.get(ch); k++) {
            if (secondString[k] === ch)
                aCount++;
        }
        ans += iCount * aCount;
    }
    return ans;
}
