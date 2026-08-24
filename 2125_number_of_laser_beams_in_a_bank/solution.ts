// LeetCode 2125 - Number of Laser Beams in a Bank
// https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

export function numberOfBeams(bank: string[]): number {
    let ans = 0, prev = 0;
    for (const row of bank) {
        let cnt = 0;
        for (let i = 0; i < row.length; i++) if (row[i] === '1') cnt++;
        if (cnt > 0) {
            ans += prev * cnt;
            prev = cnt;
        }
    }
    return ans;
}
