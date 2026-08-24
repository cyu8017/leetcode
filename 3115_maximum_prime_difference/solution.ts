// LeetCode 3115 - Maximum Prime Difference
// https://leetcode.com/problems/maximum-prime-difference/

export function maximumPrimeDifference(nums: number[]): number {
    const isPrime = (n) => {
        if (n < 2) return false;
        for (let i = 2; i * i <= n; i++) if (n % i === 0) return false;
        return true;
    };
    for (let i = 0; ; i++) {
        if (isPrime(nums[i])) {
            for (let j = nums.length - 1; ; j--) {
                if (isPrime(nums[j])) return j - i;
            }
        }
    }
}
