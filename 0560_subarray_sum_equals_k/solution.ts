// LeetCode 0560 - Subarray Sum Equals K
// https://leetcode.com/problems/subarray-sum-equals-k/

export function subarraySum(nums: number[], k: number): number {
    const counts = new Map([[0, 1]]);
    let prefix = 0, answer = 0;
    for (const num of nums) {
        prefix += num;
        answer += counts.get(prefix - k) || 0;
        counts.set(prefix, (counts.get(prefix) || 0) + 1);
    }
    return answer;
}
