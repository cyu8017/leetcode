// LeetCode 3916 - Number of ZigZag Arrays III
// https://leetcode.com/problems/number-of-zigzag-arrays-iii/

function powm3916(a, e, mod) {
    let res = 1n;
    let A = BigInt(a), E = BigInt(e), MOD = BigInt(mod);
    while (E > 0n) {
        if ((E & 1n) !== 0n) res = res * A % MOD;
        A = A * A % MOD;
        E >>= 1n;
    }
    return Number(res);
}
var zigZagArrays = function(n, l, r) {
    const mod = 1000000007;
    const points = n + 1;
    const values = new Array(points + 1).fill(0);
    for (let m = 1; m <= points; m++) {
        let up = new Array(m);
        let down = new Array(m);
        for (let value = 0; value < m; value++) {
            up[value] = value;
            down[value] = m - 1 - value;
        }
        for (let length = 3; length <= n; length++) {
            const nextUp = new Array(m).fill(0);
            const nextDown = new Array(m).fill(0);
            let prefix = 0;
            for (let value = 0; value < m; value++) {
                nextUp[value] = prefix;
                prefix = (prefix + down[value]) % mod;
            }
            let suffix = 0;
            for (let value = m - 1; value >= 0; value--) {
                nextDown[value] = suffix;
                suffix = (suffix + up[value]) % mod;
            }
            up = nextUp;
            down = nextDown;
        }
        for (let value = 0; value < m; value++) {
            values[m] = (values[m] + up[value] + down[value]) % mod;
        }
    }
    const x = (r - l + 1) % mod;
    if (r - l + 1 <= points) return values[r - l + 1];
    const prefixA = new Array(points + 2);
    const suffixA = new Array(points + 2);
    prefixA[0] = 1;
    for (let i = 1; i <= points; i++) {
        prefixA[i] = Number(BigInt(prefixA[i - 1]) * BigInt((x - i + mod) % mod) % BigInt(mod));
    }
    suffixA[points + 1] = 1;
    for (let i = points; i >= 1; i--) {
        suffixA[i] = Number(BigInt(suffixA[i + 1]) * BigInt((x - i + mod) % mod) % BigInt(mod));
    }
    const factorial = new Array(points + 1);
    factorial[0] = 1;
    for (let i = 1; i <= points; i++) factorial[i] = Number(BigInt(factorial[i - 1]) * BigInt(i) % BigInt(mod));
    let answer = 0;
    for (let i = 1; i <= points; i++) {
        const numerator = Number(BigInt(prefixA[i - 1]) * BigInt(suffixA[i + 1]) % BigInt(mod));
        const denominator = Number(BigInt(factorial[i - 1]) * BigInt(factorial[points - i]) % BigInt(mod));
        let term = Number(BigInt(values[i]) * BigInt(numerator) % BigInt(mod) * BigInt(powm3916(denominator, mod - 2, mod)) % BigInt(mod));
        if ((points - i) % 2 === 1) answer -= term;
        else answer += term;
        answer %= mod;
    }
    if (answer < 0) answer += mod;
    return answer;
};
