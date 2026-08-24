// LeetCode 2543 - Check if Point Is Reachable
// https://leetcode.com/problems/check-if-point-is-reachable/

export function isReachable(targetX: number, targetY: number): boolean {
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    let g = gcd(targetX, targetY);
    while (g % 2 === 0) g = Math.floor(g / 2);
    return g === 1;
}
