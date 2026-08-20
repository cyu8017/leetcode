// LeetCode 1189 - Maximum Number of Balloons
// https://leetcode.com/problems/maximum-number-of-balloons/

function maxNumberOfBalloons(text: string): number {
    const count = {};
    for (const ch of text) count[ch] = (count[ch] || 0) + 1;
    return Math.min(count.b || 0, count.a || 0, Math.floor((count.l || 0) / 2), Math.floor((count.o || 0) / 2), count.n || 0);
}
