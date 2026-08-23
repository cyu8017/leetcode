// LeetCode 2201 - Count Artifacts That Can Be Extracted
// https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

/**
 * @param {number} n
 * @param {number[][]} artifacts
 * @param {number[][]} dig
 * @return {number}
 */
var digArtifacts = function(n, artifacts, dig) {
    const dug = new Set();
    for (const d of dig) dug.add(d[0] + ',' + d[1]);
    let ans = 0;
    for (const a of artifacts) {
        let ok = true;
        for (let r = a[0]; r <= a[2] && ok; r++)
            for (let c = a[1]; c <= a[3]; c++)
                if (!dug.has(r + ',' + c)) { ok = false; break; }
        if (ok) ans++;
    }
    return ans;
};
