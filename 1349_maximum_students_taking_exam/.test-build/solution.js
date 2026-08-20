"use strict";
// LeetCode 1349 - Maximum Students Taking Exam
// https://leetcode.com/problems/maximum-students-taking-exam/
function maxStudents(seats) {
    const rows = seats.length, cols = seats[0].length;
    const validRows = seats.map((row) => {
        let available = 0;
        for (let c = 0; c < cols; c++)
            if (row[c] === ".")
                available |= 1 << c;
        const masks = [];
        for (let mask = 0; mask < (1 << cols); mask++) {
            if ((mask & ~available) === 0 && (mask & (mask << 1)) === 0)
                masks.push(mask);
        }
        return masks;
    });
    let dp = new Map([[0, 0]]);
    for (const masks of validRows) {
        const nxt = new Map();
        for (const mask of masks) {
            for (const [previous, count] of dp) {
                if ((mask & (previous << 1)) === 0 && (mask & (previous >> 1)) === 0) {
                    const bits = mask.toString(2).split("1").length - 1;
                    nxt.set(mask, Math.max(nxt.get(mask) || 0, count + bits));
                }
            }
        }
        dp = nxt;
    }
    return Math.max(...dp.values());
}
