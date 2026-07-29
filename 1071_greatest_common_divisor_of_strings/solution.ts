// LeetCode 1071 - Greatest Common Divisor of Strings
// https://leetcode.com/problems/greatest-common-divisor-of-strings/

function gcdOfStrings(str1: string, str2: string): string {
    if (str1 + str2 !== str2 + str1) return "";
    function gcd(a: number, b: number): number {
        while (b) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
    return str1.slice(0, gcd(str1.length, str2.length));
}
