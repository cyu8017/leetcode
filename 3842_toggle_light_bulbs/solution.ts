// LeetCode 3842 - Toggle Light Bulbs
// https://leetcode.com/problems/toggle-light-bulbs/

export function toggleLightBulbs(bulbs: any): any {
    const st = new Array(101).fill(0);
    for (const x of bulbs) st[x] ^= 1;
    const ans = [];
    for (let i = 0; i < 101; i++) if (st[i] === 1) ans.push(i);
    return ans;
}
