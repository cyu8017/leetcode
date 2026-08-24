// LeetCode 3984 - Divisible Game
// https://leetcode.com/problems/divisible-game/
var divisibleGame = function(nums) {
        let candidates = new Set();
        candidates.push(2);
        for (const value of nums) {
            for (let divisor = 2; divisor * divisor <= value; divisor++) {
                if (value % divisor != 0) continue;
                candidates.push(divisor);
                candidates.push(value / divisor);
            }
            if (value > 1) candidates.push(value);
        }
        let bestScore = -(1 << 62);
        let bestK = 0;
        for (const k of candidates) {
            let ending = 0, score = 0;
            for (let i = 0; i < nums.length; i++) {
                let value = nums[i];
                let contribution = -(value);
                if (value % k == 0) contribution = value;
                if (i == 0 || ending + contribution < contribution) ending = contribution;
                else ending += contribution;
                if (i == 0 || ending > score) score = ending;
            }
            if (score > bestScore || (score == bestScore && k < bestK)) {
                bestScore = score;
                bestK = k;
            }
        }
        let mod = 1000000007;
        let answer = (bestScore % mod) * bestK % mod;
        if (answer < 0) answer += mod;
        return answer;
    
};
