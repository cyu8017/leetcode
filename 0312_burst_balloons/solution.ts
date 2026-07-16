// LeetCode 0312 - Burst Balloons
export function maxCoins(nums: number[]): number {
    const balloons = [1, ...nums, 1];
    const size = balloons.length;
    const dp = Array.from({ length: size }, () => Array(size).fill(0));
    for (let length = 3; length <= size; length += 1) {
        for (let left = 0; left <= size - length; left += 1) {
            const right = left + length - 1;
            for (let mid = left + 1; mid < right; mid += 1) {
                dp[left][right] = Math.max(
                    dp[left][right],
                    dp[left][mid] + dp[mid][right] + balloons[left] * balloons[mid] * balloons[right],
                );
            }
        }
    }
    return dp[0][size - 1];
}
