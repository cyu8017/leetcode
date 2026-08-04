// LeetCode 1411: Number Of Ways To Paint N 3 Grid

var numOfWays = function(n) {
    const mod = 1000000007;
    let two = 6, three = 6;
    for (let row = 2; row <= n; row++) [two, three] = [(3 * two + 2 * three) % mod, (2 * two + 2 * three) % mod];
    return (two + three) % mod;
};
