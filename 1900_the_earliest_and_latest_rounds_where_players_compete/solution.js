// LeetCode 1900 - The Earliest and Latest Rounds Where Players Compete
// https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

/**
 * @param {number} n
 * @param {number} firstPlayer
 * @param {number} secondPlayer
 * @return {number[]}
 */
var earliestAndLatest = function(n, firstPlayer, secondPlayer) {
    const first = firstPlayer;
    const second = secondPlayer;
    const memo = new Map();

    const product = (choices) => {
        let results = [[]];
        for (const options of choices) {
            const next = [];
            for (const prefix of results) {
                for (const option of options) {
                    next.push([...prefix, option]);
                }
            }
            results = next;
        }
        return results;
    };

    const dfs = (players) => {
        const key = players.join(",");
        if (memo.has(key)) return memo.get(key);
        const count = players.length;
        const firstIndex = players.indexOf(first);
        const secondIndex = players.indexOf(second);
        if (firstIndex + secondIndex === count - 1) {
            const res = [1, 1];
            memo.set(key, res);
            return res;
        }

        const choices = [];
        for (let index = 0; index < Math.floor(count / 2); index++) {
            const left = players[index];
            const right = players[count - 1 - index];
            if (left === first || left === second) choices.push([left]);
            else if (right === first || right === second) choices.push([right]);
            else choices.push([left, right]);
        }
        if (count % 2) choices.push([players[Math.floor(count / 2)]]);

        let earliest = 1e9, latest = 0;
        for (const picks of product(choices)) {
            const winners = picks.slice().sort((a, b) => a - b);
            const [early, late] = dfs(winners);
            earliest = Math.min(earliest, early + 1);
            latest = Math.max(latest, late + 1);
        }
        const res = [earliest, latest];
        memo.set(key, res);
        return res;
    };

    return dfs(Array.from({ length: n }, (_, i) => i + 1));
};
