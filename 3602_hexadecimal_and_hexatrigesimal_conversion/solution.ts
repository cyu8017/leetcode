// LeetCode 3602 - Hexadecimal and Hexatrigesimal Conversion
// https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/

function f3602(x: any, k: any): any {
    let res = '';
    while (x > 0) {
        const v = x % k;
        res += v <= 9 ? String.fromCharCode(48 + v) : String.fromCharCode(65 + v - 10);
        x = Math.floor(x / k);
    }
    return res.split('').reverse().join('');
}export function concatHex36(n: any): any {
    return f3602(n * n, 16) + f3602(n * n * n, 36);
}
