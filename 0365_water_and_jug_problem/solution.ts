const gcd = (a: number, b: number): number => (b === 0 ? a : gcd(b, a % b));

export function canMeasureWater(x: number, y: number, target: number): boolean {
    if (target === 0) return true;
    if (x + y < target) return false;
    return target % gcd(x, y) === 0;
}
