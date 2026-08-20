"use strict";
function getProbability(balls) {
    const half = balls.reduce((sum, value) => sum + value, 0) / 2;
    const choose = (n, k) => {
        k = Math.min(k, n - k);
        let result = 1;
        for (let i = 1; i <= k; i++)
            result = result * (n - k + i) / i;
        return result;
    };
    let good = 0, total = 0;
    const dfs = (index, leftCount, distinctDifference, ways) => {
        if (index === balls.length) {
            if (leftCount === half) {
                total += ways;
                if (distinctDifference === 0)
                    good += ways;
            }
            return;
        }
        for (let left = 0; left <= balls[index] && leftCount + left <= half; left++) {
            dfs(index + 1, leftCount + left, distinctDifference + (left > 0 ? 1 : 0) - (left < balls[index] ? 1 : 0), ways * choose(balls[index], left));
        }
    };
    dfs(0, 0, 0, 1);
    return good / total;
}
