// LeetCode 1753 - Maximum Score From Removing Stones
// https://leetcode.com/problems/maximum-score-from-removing-stones/

function maximumScore(a: number, b: number, c: number): number {
    const stones = [a, b, c].sort((x, y) => y - x);
    let score = 0;
    while (stones[0] > 0 && stones[1] > 0) {
        stones[0]--;
        stones[1]--;
        score++;
        stones.sort((x, y) => y - x);
    }
    return score;
}
