function getProbability(balls: any): any {
    const half = balls.reduce((sum, value: any): any => sum + value, 0) / 2;
    const choose = (n: any, k: any): any => {
        k = Math.min(k, n - k);
        let result = 1;
        for (let i = 1; i <= k; i++) result = result * (n - k + i) / i;
        return result;
    };
    let good = 0, total = 0;
    const dfs = (index: any, leftCount: any, distinctDifference: any, ways: any): any => {
        if (index === balls.length) {
            if (leftCount === half) {
                total += ways;
                if (distinctDifference === 0) good += ways;
            }
            return;
        }
        for (let left = 0; left <= balls[index] && leftCount + left <= half; left++) {
            dfs(index + 1, leftCount + left,
                distinctDifference + (left > 0 ? 1 : 0) - (left < balls[index] ? 1 : 0),
                ways * choose(balls[index], left));
        }
    };
    dfs(0, 0, 0, 1);
    return good / total;
}
