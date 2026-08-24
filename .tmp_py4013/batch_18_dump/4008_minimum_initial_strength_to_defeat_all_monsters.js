// LeetCode 4008 - Minimum Initial Strength to Defeat All Monsters
// https://leetcode.com/problems/minimum-initial-strength-to-defeat-all-monsters/
var minInitialStrength = function(monsters, boosts) {
        let n = monsters.length;
        let d = new Array(n + 1).fill(0);
        for (const b of boosts) {
            d[b[0]] += b[2];
            d[b[1] + 1] -= b[2];
        }
        let left = 0, right = 1000000000000000;
        while (left < right) {
            let mid = (left + right) / 2;
            if (check(mid, monsters, d)) right = mid;
            else left = mid + 1;
        }
        return left;
    
};
var check = function(v, monsters, d) {
        let bonus = 0;
        for (let i = 0; i < monsters.length; i++) {
            bonus += d[i];
            if (v + bonus < monsters[i]) return false;
            v -= monsters[i];
            if (v < 0) v = 0;
        }
        return true;
    
};
