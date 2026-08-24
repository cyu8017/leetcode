// LeetCode 0650 - 2 Keys Keyboard
// https://leetcode.com/problems/2-keys-keyboard/

export function minSteps(n: number): number {
    let steps = 0, factor = 2;
    while (factor * factor <= n) {
        while (n % factor === 0) {
            steps += factor;
            n = Math.floor(n / factor);
        }
        ++factor;
    }
    if (n > 1) steps += n;
    return steps;
}
