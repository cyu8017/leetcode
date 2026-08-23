// LeetCode 3147 - Taking Maximum Energy From the Mystic Dungeon
// https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

/**
 * @param {number[]} energy
 * @param {number} k
 * @return {number}
 */
var maximumEnergy = function(energy, k) {
    let ans = -(1 << 30);
    const n = energy.length;
    for (let i = n - k; i < n; i++) {
        for (let j = i, s = 0; j >= 0; j -= k) {
            s += energy[j];
            ans = Math.max(ans, s);
        }
    }
    return ans;
};
