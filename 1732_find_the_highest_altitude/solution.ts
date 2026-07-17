// LeetCode 1732 - Find the Highest Altitude
// https://leetcode.com/problems/find-the-highest-altitude/

function largestAltitude(gain: number[]): number {
    let altitude = 0;
    let best = 0;
    for (const change of gain) {
        altitude += change;
        best = Math.max(best, altitude);
    }
    return best;
}
