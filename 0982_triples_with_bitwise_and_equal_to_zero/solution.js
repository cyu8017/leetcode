// LeetCode 0982 - Triples with Bitwise AND Equal To Zero
// https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

/**
 * @param {number[]} nums
 * @return {number}
 */
var countTriplets = function(nums) {
    const cnt = new Map();
    for (const a of nums)
        for (const b of nums)
            cnt.set(a & b, (cnt.get(a & b) || 0) + 1);
    let ans = 0;
    for (const c of nums)
        for (const [k, v] of cnt)
            if ((k & c) === 0) ans += v;
    return ans;
};
