// LeetCode 3987 - Minimum Total Cost to Process All Elements
// https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/
var minimumCost = function(nums, k) {
        let mod = 1000000007;
        let cnt = 0;
        let cur = k;
        for (const x0 of nums) {
            let x = x0;
            let diff = x - cur;
            if (diff > 0) {
                let m = (diff + k - 1) / k;
                cur += m * k;
                cnt += m;
            }
            cur -= x;
        }
        cnt %= mod;
        return ((cnt + 1) * cnt / 2 % mod);
    
};
