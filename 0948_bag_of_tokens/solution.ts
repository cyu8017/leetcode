// LeetCode 0948 - Bag of Tokens
// https://leetcode.com/problems/bag-of-tokens/

export function bagOfTokensScore(tokens: number[], power: number): number {
    tokens.sort((a, b) => a - b);
    let i = 0, j = tokens.length - 1, score = 0, ans = 0;
    while (i <= j) {
        if (power >= tokens[i]) {
            power -= tokens[i++];
            score++;
            ans = Math.max(ans, score);
        } else if (score > 0) {
            power += tokens[j--];
            score--;
        } else break;
    }
    return ans;
}
