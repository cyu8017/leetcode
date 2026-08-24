// LeetCode 3918 - Sum Of Primes Between Number And Its Reverse
// https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

let isPrime3918 = null;
function Init3918(): any {
    if (isPrime3918) return;
    isPrime3918 = new Array(1001).fill(true);
    isPrime3918[0] = isPrime3918[1] = false;
    for (let i = 2; i * i <= 1000; i++) {
        if (isPrime3918[i]) {
            for (let j = i * i; j <= 1000; j += i) isPrime3918[j] = false;
        }
    }
}export function sumOfPrimesInRange(n: any): any {
    Init3918();
    let r = 0;
    for (let x = n; x > 0; x = Math.floor(x / 10)) r = r * 10 + x % 10;
    const low = Math.min(n, r), high = Math.max(n, r);
    let ans = 0;
    for (let x = low; x <= high; x++) {
        if (isPrime3918[x]) ans += x;
    }
    return ans;
}
