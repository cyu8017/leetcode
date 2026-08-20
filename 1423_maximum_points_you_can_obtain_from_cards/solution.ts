function maxScore(cardPoints: any, k: any): any {
    const n = cardPoints.length, total = cardPoints.reduce((a, b: any): any => a + b, 0);
    if (k === n) return total;
    let sum = 0, smallest = Infinity;
    for (let i = 0; i < n - k; i++) sum += cardPoints[i];
    smallest = sum;
    for (let i = n - k; i < n; i++) { sum += cardPoints[i] - cardPoints[i - (n - k)]; smallest = Math.min(smallest, sum); }
    return total - smallest;
}
