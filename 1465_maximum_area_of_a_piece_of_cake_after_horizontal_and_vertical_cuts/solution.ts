function maxArea(h: any, w: any, horizontalCuts: any, verticalCuts: any): any {
    const largestGap = (cuts: any, end: any): any => {
        cuts.sort((a, b: any): any => a - b);
        let best = cuts[0], previous = 0;
        for (const cut of cuts) {
            best = Math.max(best, cut - previous);
            previous = cut;
        }
        return Math.max(best, end - previous);
    };
    const mod = 1000000007n;
    return Number((BigInt(largestGap(horizontalCuts, h)) * BigInt(largestGap(verticalCuts, w))) % mod);
}
