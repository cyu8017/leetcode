// LeetCode 3494 - Find the Minimum Amount of Time to Brew Potions
// https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

var minTime = function(skill, mana) {
    const n = skill.length, m = mana.length;
    const done = new Array(n).fill(0);
    for (let j = 0; j < m; j++) {
        let t = 0;
        for (let i = 0; i < n; i++) {
            if (done[i] > t) t = done[i];
            t += skill[i] * mana[j];
            done[i] = t;
        }
        for (let i = n - 2; i >= 0; i--)
            done[i] = done[i + 1] - skill[i + 1] * mana[j];
    }
    return done[n - 1];
};
