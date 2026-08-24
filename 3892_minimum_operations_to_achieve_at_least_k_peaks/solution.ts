// LeetCode 3892 - Minimum Operations to Achieve At Least K Peaks
// https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

export function minOperations(nums: any, k: any): any {
    const INF = Number.MAX_SAFE_INTEGER / 4;
    const n = nums.length;
    if (k === 0) return 0;
    if (k > Math.floor(n / 2)) return -1;
    const cost = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        const left = nums[(i + n - 1) % n], right = nums[(i + 1) % n];
        const need = Math.max(left, right);
        if (need >= nums[i]) cost[i] = need - nums[i] + 1;
    }
    const line = (left, right, choose) => {
        if (choose === 0) return 0;
        if (left > right || choose > Math.floor((right - left + 2) / 2)) return INF;
        let prev2 = new Array(choose + 1).fill(INF);
        let prev1 = new Array(choose + 1).fill(INF);
        prev2[0] = prev1[0] = 0;
        for (let i = left; i <= right; i++) {
            const current = prev1.slice();
            for (let j = 1; j <= choose; j++) {
                if (prev2[j - 1] !== INF && prev2[j - 1] + cost[i] < current[j]) {
                    current[j] = prev2[j - 1] + cost[i];
                }
            }
            prev2 = prev1;
            prev1 = current;
        }
        return prev1[choose];
    };
    let answer = line(1, n - 1, k);
    let withFirst = line(2, n - 2, k - 1);
    if (withFirst !== INF) {
        withFirst += cost[0];
        answer = Math.min(answer, withFirst);
    }
    if (answer === INF) return -1;
    return answer;
}
