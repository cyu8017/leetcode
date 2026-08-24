// LeetCode 2511 - Maximum Enemy Forts That Can Be Captured
// https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

export function captureForts(forts: number[]): number {
    let ans = 0, prev = -1;
    for (let i = 0; i < forts.length; i++) {
        if (forts[i] !== 0) {
            if (prev >= 0 && forts[prev] === -forts[i]) {
                if (i - prev - 1 > ans) ans = i - prev - 1;
            }
            prev = i;
        }
    }
    return ans;
}
