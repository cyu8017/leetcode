// LeetCode 1952 - Three Divisors
// https://leetcode.com/problems/three-divisors/

function isThree(n: number): boolean {
    const root = Math.floor(Math.sqrt(n));
    if (root * root !== n || root < 2) return false;
    for (let i = 2; i * i <= root; i++) if (root % i === 0) return false;
    return true;
}
