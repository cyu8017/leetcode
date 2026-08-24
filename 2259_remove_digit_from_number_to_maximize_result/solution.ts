// LeetCode 2259 - Remove Digit From Number to Maximize Result
// https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

export function removeDigit(number: string, digit: string): string {
    let best = '';
    for (let i = 0; i < number.length; i++) {
        if (number[i] === digit) {
            const cand = number.slice(0, i) + number.slice(i + 1);
            if (cand > best) best = cand;
        }
    }
    return best;
}
