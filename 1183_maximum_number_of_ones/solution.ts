// LeetCode 1183 - Maximum Number of Ones
// https://leetcode.com/problems/maximum-number-of-ones/

function maximumNumberOfOnes(width: number, height: number, sideLength: number, maxOnes: number): number {
    const counts = [];
    for (let r = 0; r < sideLength; r++) {
        for (let c = 0; c < sideLength; c++) {
            const rows = Math.floor((height - r + sideLength - 1) / sideLength);
            const cols = Math.floor((width - c + sideLength - 1) / sideLength);
            counts.push(rows * cols);
        }
    }
    counts.sort((a, b) => b - a);
    let ans = 0;
    for (let i = 0; i < maxOnes; i++) ans += counts[i];
    return ans;
}
