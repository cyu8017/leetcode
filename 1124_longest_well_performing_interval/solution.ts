// LeetCode 1124 - Longest Well-Performing Interval
// https://leetcode.com/problems/longest-well-performing-interval/

function longestWPI(hours: number[]): number {
    let score = 0;
    const firstSeen = new Map([[0, -1]]);
    let ans = 0;
    for (let i = 0; i < hours.length; i++) {
        score += hours[i] > 8 ? 1 : -1;
        if (score > 0) {
            ans = i + 1;
        } else if (firstSeen.has(score - 1)) {
            ans = Math.max(ans, i - firstSeen.get(score - 1));
        }
        if (!firstSeen.has(score)) firstSeen.set(score, i);
    }
    return ans;
}
