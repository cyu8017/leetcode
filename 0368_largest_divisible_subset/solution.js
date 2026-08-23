// LeetCode 0368 - Largest Divisible Subset
var largestDivisibleSubset = function(nums) {
    nums.sort((a, b) => a - b);
    const chains = new Map(nums.map((num) => [num, [num]]));
    let best = [];

    for (const num of nums) {
        for (const [prev, chain] of chains.entries()) {
            if (prev < num && num % prev === 0 && chain.length + 1 > chains.get(num).length) {
                chains.set(num, [...chain, num]);
            }
        }
        if (chains.get(num).length > best.length) best = chains.get(num);
    }

    return best;
};
