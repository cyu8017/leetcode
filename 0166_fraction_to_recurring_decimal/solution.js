// LeetCode 0166 - Fraction to Recurring Decimal
// https://leetcode.com/problems/fraction-to-recurring-decimal/

/**
 * Converts a fraction to decimal notation, marking repeating digits.
 * @param {number} numerator
 * @param {number} denominator
 * @return {string}
 */
var fractionToDecimal = function(numerator, denominator) {
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

    const result = [sign + String(integer), '.'];
    const seen = new Map();
    while (remainder !== 0) {
        if (seen.has(remainder)) {
            result.splice(seen.get(remainder), 0, '(');
            result.push(')');
            break;
        }
        seen.set(remainder, result.length);
        remainder *= 10;
        result.push(String(Math.floor(remainder / denominator)));
        remainder %= denominator;
    }
    return result.join('');
};