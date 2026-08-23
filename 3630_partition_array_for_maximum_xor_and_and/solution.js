// LeetCode 3630 - Partition Array for Maximum XOR and AND
// https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/

var maximizeXorAndXor = function(nums) {
    const n = nums.length;
    let best = 0;
    for (let mask = 0; mask < (1 << n); mask++) {
        let andVal = -1, xorRest = 0;
        for (let i = 0; i < n; i++) {
            if (((mask >> i) & 1) !== 0) {
                andVal = andVal < 0 ? nums[i] : (andVal & nums[i]);
            } else {
                xorRest ^= nums[i];
            }
        }
        if (andVal < 0) andVal = 0;
        const comp = ((1 << n) - 1) ^ mask;
        for (let sub = comp; ; sub = (sub - 1) & comp) {
            let x1 = 0;
            for (let i = 0; i < n; i++)
                if (((sub >> i) & 1) !== 0) x1 ^= nums[i];
            const x2 = xorRest ^ x1;
            best = Math.max(best, andVal + x1 + x2);
            if (sub === 0) break;
        }
    }
    return best;
};
