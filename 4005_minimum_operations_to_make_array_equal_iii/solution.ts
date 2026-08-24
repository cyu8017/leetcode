// LeetCode 4005 - Minimum Operations to Make Array Equal III
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-iii/

export function Cost(x: any, t: any): any {
        if (x == t) return 0;
        if (x % t == 0 || t % x == 0) return 1;
        return 2;
    
}export function Gcd(a: any, b: any): any {
        while (b != 0) { let t = a % b; a = b; b = t; }
        return a;
    
}export function minOperations(nums: any): any {
        let n = nums.length;
        if (n <= 1) return 0;
        let g = nums[0], mn = nums[0];
        for (let i = 1; i < n; i++) {
            g = Gcd(g, nums[i]);
            mn = Math.min(mn, nums[i]);
        }
        var cands = new Set();
        for (const x of nums) cands.push(x);
        for (let d = 1; 1 * d * d <= mn; d++) {
            if (mn % d == 0) {
                cands.push(d);
                cands.push(mn / d);
            }
        }
        cands.push(g);
        let ans = 2147483647;
        for (const t of cands) {
            let sum = 0;
            for (const x of nums) {
                sum += Cost(x, t);
                if (sum >= ans) break;
            }
            ans = Math.min(ans, sum);
        }
        return ans;
    
}
