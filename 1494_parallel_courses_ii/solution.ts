function minNumberOfSemesters(n: any, relations: any, k: any): any {
    const prereq = Array(n).fill(0), full = (1 << n) - 1, dp = Array(1 << n).fill(Infinity);
    for (const [before, after] of relations) prereq[after - 1] |= 1 << (before - 1);
    dp[0] = 0;
    const bitCount = (value: any): any => {
        let count = 0;
        while (value) {
            value &= value - 1;
            count++;
        }
        return count;
    };
    for (let mask = 0; mask <= full; mask++) {
        if (dp[mask] === Infinity) continue;
        let available = 0;
        for (let course = 0; course < n; course++) {
            if (!(mask & (1 << course)) && (prereq[course] & mask) === prereq[course]) available |= 1 << course;
        }
        if (bitCount(available) <= k) dp[mask | available] = Math.min(dp[mask | available], dp[mask] + 1);
        else for (let subset = available; subset; subset = (subset - 1) & available) {
            if (bitCount(subset) === k) dp[mask | subset] = Math.min(dp[mask | subset], dp[mask] + 1);
        }
    }
    return dp[full];
}
