// LeetCode 1679 - Max Number of K-Sum Pairs
// https://leetcode.com/problems/max-number-of-k-sum-pairs/

function maxOperations(nums: number[], k: number): number {
    const c = new Map<number, number>();
    let ans = 0;
    for (const x of nums) {
        const need = k - x;
        if ((c.get(need) || 0) > 0) {
            c.set(need, c.get(need)! - 1);
            ans++;
        } else {
            c.set(x, (c.get(x) || 0) + 1);
        }
    }
    return ans;
}
