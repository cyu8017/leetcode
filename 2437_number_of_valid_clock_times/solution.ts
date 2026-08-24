// LeetCode 2437 - Number of Valid Clock Times
// https://leetcode.com/problems/number-of-valid-clock-times/

export function countTime(time: string): number {
    let ans = 0;
    for (let h = 0; h < 24; h++) {
        for (let m = 0; m < 60; m++) {
            const h0 = String(Math.floor(h / 10)), h1 = String(h % 10);
            const m0 = String(Math.floor(m / 10)), m1 = String(m % 10);
            if (time[0] !== '?' && time[0] !== h0) continue;
            if (time[1] !== '?' && time[1] !== h1) continue;
            if (time[3] !== '?' && time[3] !== m0) continue;
            if (time[4] !== '?' && time[4] !== m1) continue;
            ans++;
        }
    }
    return ans;
}
