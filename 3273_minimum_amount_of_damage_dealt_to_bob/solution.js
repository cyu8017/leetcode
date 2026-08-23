// LeetCode 3273 - Minimum Amount of Damage Dealt to Bob
// https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/

var minDamage = function(power, damage, health) {
    const n = damage.length;
    const arr = [];
    let totalDmg = 0;
    for (let i = 0; i < n; i++) {
        const hits = Math.floor((health[i] + power - 1) / power);
        arr.push({dmg: damage[i], hits});
        totalDmg += damage[i];
    }
    arr.sort((a, b) => a.hits * b.dmg - b.hits * a.dmg);
    let ans = 0, cur = totalDmg;
    for (const e of arr) {
        ans += cur * e.hits;
        cur -= e.dmg;
    }
    return ans;
};
