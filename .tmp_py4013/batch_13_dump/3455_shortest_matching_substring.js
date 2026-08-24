// LeetCode 3455 - Shortest Matching Substring
// https://leetcode.com/problems/shortest-matching-substring/

var shortestMatchingSubstring = function(s, p) {
    const parts = [];
    let cur = "";
    for (const c of p) {
        if (c === "*") {
            parts.push(cur);
            cur = "";
        } else cur += c;
    }
    parts.push(cur);
    while (parts.length < 3) parts.push("");
    const a = parts[0], b = parts[1], c = parts[2];
    const n = s.length;
    const findAll = (sub) => {
        const res = [];
        if (sub.length === 0) {
            for (let i = 0; i <= n; i++) res.push(i);
            return res;
        }
        for (let i = 0; i + sub.length <= n; i++) {
            if (s.startsWith(sub, i)) res.push(i);
        }
        return res;
    };
    const sortSearch = (arr, x) => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    const posA = findAll(a), posB = findAll(b), posC = findAll(c);
    let ans = n + 1;
    for (const ia of posA) {
        const endA = ia + a.length;
        let bi = sortSearch(posB, endA);
        for (; bi < posB.length; bi++) {
            const endB = posB[bi] + b.length;
            const ci = sortSearch(posC, endB);
            if (ci < posC.length) {
                const length = posC[ci] + c.length - ia;
                if (length < ans) ans = length;
            }
            break;
        }
    }
    return ans === n + 1 ? -1 : ans;
};
