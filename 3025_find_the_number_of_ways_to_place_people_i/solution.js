// LeetCode 3025 - Find the Number of Ways to Place People I
// https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/

var numberOfPairs = function(points) {
    points.sort((a, b) => a[0] !== b[0] ? a[0] - b[0] : b[1] - a[1]);
    let ans = 0;
    for (let i = 0; i < points.length; i++) {
        const y1 = points[i][1];
        let maxY = -Infinity;
        for (let j = i + 1; j < points.length; j++) {
            const y2 = points[j][1];
            if (maxY < y2 && y2 <= y1) {
                maxY = y2;
                ans++;
            }
        }
    }
    return ans;
};
