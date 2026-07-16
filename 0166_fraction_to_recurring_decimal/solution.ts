// LeetCode 0166 - Fraction to Recurring Decimal
// https://leetcode.com/problems/fraction-to-recurring-decimal/

export function fractionToDecimal(numerator: number, denominator: number): string {
    if (numerator === 0) {
        return '0';
    }

    const sign = (numerator < 0) !== (denominator < 0) ? '-' : '';
    numerator = Math.abs(numerator);
    denominator = Math.abs(denominator);
    const integer = Math.floor(numerator / denominator);
    let remainder = numerator % denominator;
    if (remainder === 0) {
        return sign + String(integer);
    }

    const result: string[] = [sign + String(integer), '.'];
    const seen = new Map<number, number>();
    while (remainder !== 0) {
        const repeatIndex = seen.get(remainder);
        if (repeatIndex !== undefined) {
            result.splice(repeatIndex, 0, '(');
            result.push(')');
            break;
        }
        seen.set(remainder, result.length);
        remainder *= 10;
        result.push(String(Math.floor(remainder / denominator)));
        remainder %= denominator;
    }
    return result.join('');
}