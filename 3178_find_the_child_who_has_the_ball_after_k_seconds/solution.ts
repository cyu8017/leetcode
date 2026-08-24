// LeetCode 3178 - Find the Child Who Has the Ball After K Seconds
// https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/

export function numberOfChild(n: any, k: any): any {
    let mod = k % (n - 1);
    k = Math.floor(k / (n - 1));
    if (k % 2 === 1) return n - mod - 1;
    return mod;
}
