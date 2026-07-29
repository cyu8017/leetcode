// LeetCode 1010 - Pairs of Songs With Total Durations Divisible by 60
// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

function numPairsDivisibleBy60(time: number[]): number {
    const count = new Array(60).fill(0);
    let ans = 0;
    for (const t of time) {
        ans += count[(60 - (t % 60)) % 60];
        count[t % 60]++;
    }
    return ans;
}
