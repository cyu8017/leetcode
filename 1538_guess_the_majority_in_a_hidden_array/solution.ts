// LeetCode 1538 - Guess the Majority in a Hidden Array
// https://leetcode.com/problems/guess-the-majority-in-a-hidden-array/
// @ts-nocheck

function guessMajority(reader: any | number[]): number {
    if (Array.isArray(reader)) {
        const nums = reader;
        reader = {
            query(a, b, c, d) {
                const ones = nums[a] + nums[b] + nums[c] + nums[d];
                if (ones === 0 || ones === 4) return 4;
                if (ones === 1 || ones === 3) return 2;
                return 0;
            },
            length() { return nums.length; }
        };
    }
    const n = reader.length();
    const firstFour = reader.query(0, 1, 2, 3);
    const shifted = reader.query(1, 2, 3, 4);
    let same = 1, different = 0, differentIndex = -1, laterDifferent = -1;
    const fourSame = firstFour === shifted;
    if (fourSame) same++;
    else { different++; differentIndex = 4; }
    const checks = [[0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4]];
    for (let index = 0; index < checks.length; index++) {
        if (reader.query(...checks[index]) === shifted) same++;
        else { different++; differentIndex = index + 1; }
    }
    for (let i = 5; i < n; i++) {
        const iSameAsFour = reader.query(1, 2, 3, i) === shifted;
        if (iSameAsFour === fourSame) same++;
        else {
            different++;
            differentIndex = i;
            if (laterDifferent === -1) laterDifferent = i;
        }
    }
    if (same === different) return -1;
    return same > different ? 0 : (laterDifferent !== -1 ? laterDifferent : differentIndex);
}
