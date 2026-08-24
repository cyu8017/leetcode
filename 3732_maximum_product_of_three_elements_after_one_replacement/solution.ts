// LeetCode 3732 - Maximum Product of Three Elements After One Replacement
// https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

export function maxProduct(nums: any): any {
    const a = nums.slice().sort((x, y) => x - y);
    const n = a.length;
    const A = a[0], B = a[1], C = a[n - 2], D = a[n - 1];
    const x = 100000;
    return Math.max(Math.max(A * B * x, C * D * x), -A * D * x);
}
