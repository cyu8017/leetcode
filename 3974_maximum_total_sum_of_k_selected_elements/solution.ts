// LeetCode 3974 - Maximum Total Sum Of K Selected Elements
// https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/

export function maxSum(nums: any, k: any, mul: any): any {
        nums.sort((a,b)=>a-b);
        let n = nums.length;
        let ans = 0;
        for (let i = n - 1; i >= n - k; i--) {
            let m = Math.max(1, mul);
            ans += nums[i] * m;
            mul--;
        }
        return ans;
    
}
