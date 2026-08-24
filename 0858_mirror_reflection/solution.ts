// LeetCode 0858 - Mirror Reflection
// https://leetcode.com/problems/mirror-reflection/

export function mirrorReflection(p: number, q: number): number {
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    const g = gcd(p, q);
    p /= g;
    q /= g;
    if (p % 2 === 0) return 2;
    if (q % 2 === 0) return 0;
    return 1;
}
