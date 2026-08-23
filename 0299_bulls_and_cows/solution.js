// LeetCode 0299 - Bulls and Cows
// https://leetcode.com/problems/bulls-and-cows/

/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
var getHint = function(secret, guess) {
    let bulls = 0;
    const secretCounts = new Map();
    const guessCounts = new Map();
    for (let index = 0; index < secret.length; index += 1) {
        const secretDigit = secret[index];
        const guessDigit = guess[index];
        if (secretDigit === guessDigit) {
            bulls += 1;
        } else {
            secretCounts.set(secretDigit, (secretCounts.get(secretDigit) || 0) + 1);
            guessCounts.set(guessDigit, (guessCounts.get(guessDigit) || 0) + 1);
        }
    }
    let cows = 0;
    for (const [digit, count] of guessCounts) {
        cows += Math.min(count, secretCounts.get(digit) || 0);
    }
    return `${bulls}A${cows}B`;
};
