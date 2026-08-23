// LeetCode 3944 - Minimum Operations to Make Array Modulo Alternating II
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/
var minOperations = function(nums, k) {
        let evenFreq = new Array(k).fill(0), oddFreq = new Array(k).fill(0);
        for (let i = 0; i < nums.length; i++) {
            if (i % 2 == 0) evenFreq[nums[i] % k]++;
            else oddFreq[nums[i] % k]++;
        }
        let evenCost = costs(evenFreq, k);
        let oddCost = costs(oddFreq, k);
        let best1 = 1 << 62, best2 = 1 << 62;
        let bestIndex = -1;
        for (let i = 0; i < k; i++) {
            let x = oddCost[i];
            if (x < best1) {
                best2 = best1;
                best1 = x;
                bestIndex = i;
            } else if (x < best2) best2 = x;
        }
        let ans = 1 << 62;
        for (let x = 0; x < k; x++) {
            let other = (x == bestIndex) ? best2 : best1;
            ans = Math.min(ans, evenCost[x] + other);
        }
        return ans;
    
};
var costs = function(freq, k) {
        let dbl = new Array(2 * k).fill(0);
        for (let i = 0; i < 2 * k; i++) dbl[i] = freq[i % k];
        let countPrefix = new Array(2 * k + 1).fill(0), weightedPrefix = new Array(2 * k + 1).fill(0);
        for (let i = 0; i < 2 * k; i++) {
            countPrefix[i + 1] = countPrefix[i] + dbl[i];
            weightedPrefix[i + 1] = weightedPrefix[i] + i * dbl[i];
        }
        let res = new Array(k).fill(0);
        let cw = k / 2, cc = (k - 1) / 2;
        for (let t = 0; t < k; t++) {
            let cnt = countPrefix[t + cw + 1] - countPrefix[t];
            let sum = weightedPrefix[t + cw + 1] - weightedPrefix[t];
            res[t] += sum - t * cnt;
            if (cc > 0) {
                let cnt2 = countPrefix[t + k] - countPrefix[t + k - cc];
                let sum2 = weightedPrefix[t + k] - weightedPrefix[t + k - cc];
                res[t] += (t + k) * cnt2 - sum2;
            }
        }
        return res;
    
};
