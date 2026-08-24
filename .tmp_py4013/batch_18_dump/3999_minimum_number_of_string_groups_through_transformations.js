// LeetCode 3999 - Minimum Number of String Groups Through Transformations
// https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/

function leastRotation(s) {
    const n = s.length;
    let i = 0, j = 1, k = 0;
    while (i < n && j < n && k < n) {
        const a = s[(i + k) % n];
        const b = s[(j + k) % n];
        if (a === b) ++k;
        else {
            if (a > b) i += k + 1;
            else j += k + 1;
            if (i === j) ++j;
            k = 0;
        }
    }
    return i < j ? i : j;
}

function canonicalRotate(s) {
    const n = s.length;
    if (n <= 1) return s;
    const r = leastRotation(s);
    if (r === 0) return s;
    return s.slice(r) + s.slice(0, r);
}

var minimumGroups = function(words) {
    const keys = [];
    for (const w of words) {
        const n = w.length;
        let even = '', odd = '';
        for (let i = 0; i < n; i++) {
            if (i % 2 === 0) even += w[i];
            else odd += w[i];
        }
        keys.push(canonicalRotate(even) + '#' + canonicalRotate(odd));
    }
    keys.sort();
    let groups = 0;
    for (let i = 0; i < keys.length; i++) {
        if (i === 0 || keys[i] !== keys[i - 1]) ++groups;
    }
    return groups;
};
