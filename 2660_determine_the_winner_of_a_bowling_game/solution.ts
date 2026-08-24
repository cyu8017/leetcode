// LeetCode 2660 - Determine the Winner of a Bowling Game
// https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

export function isWinner(player1: any, player2: any): any {
    const score = (p) => {
        let s = 0;
        for (let i = 0; i < p.length; i++) {
            let mul = 1;
            if ((i > 0 && p[i - 1] === 10) || (i > 1 && p[i - 2] === 10)) mul = 2;
            s += mul * p[i];
        }
        return s;
    };
    const a = score(player1), b = score(player2);
    if (a > b) return 1;
    if (b > a) return 2;
    return 0;
}
