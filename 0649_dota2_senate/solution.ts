// LeetCode 0649 - Dota2 Senate
// https://leetcode.com/problems/dota2-senate/

export function predictPartyVictory(senate: string): string {
    const radiant = [], dire = [];
    const n = senate.length;
    for (let i = 0; i < n; ++i) {
        if (senate[i] === "R") radiant.push(i);
        else dire.push(i);
    }
    while (radiant.length && dire.length) {
        const r = radiant.shift(), d = dire.shift();
        if (r < d) radiant.push(r + n);
        else dire.push(d + n);
    }
    return radiant.length === 0 ? "Dire" : "Radiant";
}
