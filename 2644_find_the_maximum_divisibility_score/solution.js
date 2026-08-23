// LeetCode 2644 - Find the Maximum Divisibility Score
// https://leetcode.com/problems/find-the-maximum-divisibility-score/

var maxDivScore = function(nums, divisors) {
    let best = divisors[0], bestScore = -1;
    for (const d of divisors) {
        let score = 0;
        for (const x of nums) if (x % d === 0) score++;
        if (score > bestScore || (score === bestScore && d < best)) {
            bestScore = score;
            best = d;
        }
    }
    return best;
};
