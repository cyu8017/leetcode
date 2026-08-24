// LeetCode 3463 - Check If Digits Are Equal in String After Operations II
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/

var hasSameDigits = function(s) {
    const modPowP = (a, e, p) => {
        let r = 1;
        while (e > 0) {
            if (e % 2 === 1) r = r * a % p;
            a = a * a % p;
            e = Math.floor(e / 2);
        }
        return r;
    };
    const modInvPrime = (a, p) => modPowP(a, p - 2, p);
    const binomMod = (n, k, p) => {
        if (k < 0 || k > n) return 0;
        let num = 1, den = 1;
        for (let i = 0; i < k; i++) {
            num = num * (n - i) % p;
            den = den * (i + 1) % p;
        }
        return num * modInvPrime(den, p) % p;
    };
    const crt = (a1, m1, a2, m2) => {
        for (let x = 0; x < m1 * m2; x++) {
            if (x % m1 === a1 && x % m2 === a2) return x;
        }
        return 0;
    };
    const binomMod10 = (n, k) => crt(binomMod(n, k, 2), 2, binomMod(n, k, 5), 5);
    const combineDigit = (offset) => {
        const n = s.length;
        let sum = 0;
        for (let i = 0; i <= n - 2; i++) {
            sum = (sum + binomMod10(n - 2, i) * (s.charCodeAt(i + offset) - 48)) % 10;
        }
        return sum;
    };
    return combineDigit(0) === combineDigit(1);
};
