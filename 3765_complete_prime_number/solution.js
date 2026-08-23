// LeetCode 3765 - Complete Prime Number
// https://leetcode.com/problems/complete_prime_number/

var completePrime = function(num) {
    const isPrime = (x) => {
        if (x < 2) return false;
        for (let i = 2; i * i <= x; i++) if (x % i === 0) return false;
        return true;
    };
    const s = String(num);
    let x = 0;
    for (const c of s) {
        x = x * 10 + (c.charCodeAt(0) - 48);
        if (!isPrime(x)) return false;
    }
    x = 0;
    let p = 1;
    for (let i = s.length - 1; i >= 0; i--) {
        x = p * (s.charCodeAt(i) - 48) + x;
        p *= 10;
        if (!isPrime(x)) return false;
    }
    return true;
};
