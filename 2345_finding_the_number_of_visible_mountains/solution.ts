// LeetCode 2345 - Finding the Number of Visible Mountains
// https://leetcode.com/problems/finding-the-number-of-visible-mountains/

export function visibleMountains(peaks: number[][]): number {
    const arr = peaks.map(p => [p[0] - p[1], p[0] + p[1]]);
    arr.sort((a, b) => {
        if (a[0] === b[0]) return b[1] - a[1];
        return a[0] - b[0];
    });
    let ans = 0;
    let maxR = -Infinity;
    for (let i = 0; i < arr.length; ) {
        let j = i;
        while (j < arr.length && arr[j][0] === arr[i][0] && arr[j][1] === arr[i][1]) j++;
        if (arr[i][1] > maxR) {
            if (j - i === 1) ans++;
            maxR = arr[i][1];
        }
        i = j;
    }
    return ans;
}
