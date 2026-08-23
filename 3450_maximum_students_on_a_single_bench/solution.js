// LeetCode 3450 - Maximum Students on a Single Bench
// https://leetcode.com/problems/maximum-students-on-a-single-bench/

var maxStudentsOnBench = function(students) {
    const bench = new Map();
    for (const s of students) {
        if (!bench.has(s[1])) bench.set(s[1], new Set());
        bench.get(s[1]).add(s[0]);
    }
    let ans = 0;
    for (const set of bench.values()) {
        if (set.size > ans) ans = set.size;
    }
    return ans;
};
