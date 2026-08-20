// LeetCode 1224 - Maximum Equal Frequency
// https://leetcode.com/problems/maximum-equal-frequency/

function maxEqualFreq(nums: number[]): number {
    const count = new Map();
    const frequencies = new Map();
    let answer = 0;
    for (let i = 0; i < nums.length; i++) {
        const x = nums[i];
        const old = count.get(x) || 0;
        if (old) frequencies.set(old, (frequencies.get(old) || 0) - 1);
        count.set(x, old + 1);
        frequencies.set(old + 1, (frequencies.get(old + 1) || 0) + 1);
        const high = Math.max(...frequencies.keys());
        if (
            high === 1 ||
            (frequencies.get(high) || 0) * high + 1 === i + 1 ||
            ((frequencies.get(high) || 0) === 1 && (frequencies.get(high - 1) || 0) * (high - 1) + high === i + 1)
        ) {
            answer = i + 1;
        }
    }
    return answer;
}
