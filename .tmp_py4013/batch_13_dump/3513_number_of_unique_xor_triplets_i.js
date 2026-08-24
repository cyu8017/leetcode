// LeetCode 3513 - Number of Unique XOR Triplets I
// https://leetcode.com/problems/number-of-unique-xor-triplets-i/

var uniqueXorTriplets = function(nums) {
    const n = nums.length;
    if (n <= 2) return n;
    let x = n, len = 0;
    while (x !== 0) { len++; x >>= 1; }
    return 1 << len;
};
