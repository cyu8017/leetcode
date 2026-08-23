// LeetCode 3750 - Minimum Number Of Flips To Reverse Binary String
// https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

var minimumFlips = function(n) {
    let s;
    let x = n;
    if (x === 0) s = "0";
    else {
        let bits = '';
        while (x > 0) {
            bits += String.fromCharCode(48 + (x & 1));
            x >>= 1;
        }
        s = bits.split('').reverse().join('');
    }
    const m = s.length;
    let cnt = 0;
    for (let i = 0; i < Math.floor(m / 2); i++) {
        if (s[i] !== s[m - i - 1]) cnt++;
    }
    return cnt * 2;
};
