// LeetCode 1686 - Stone Game VI
// https://leetcode.com/problems/stone-game-vi/

function stoneGameVI(aliceValues: number[], bobValues: number[]): number {
    const order = [...Array(aliceValues.length).keys()].sort(
        (i, j) => (aliceValues[j] + bobValues[j]) - (aliceValues[i] + bobValues[i])
    );
    let score = 0;
    order.forEach((i, t) => {
        score += t % 2 === 0 ? aliceValues[i] : -bobValues[i];
    });
    return score > 0 ? 1 : score < 0 ? -1 : 0;
}
