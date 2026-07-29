// LeetCode 1058 - Minimize Rounding Error to Meet Target
// https://leetcode.com/problems/minimize-rounding-error-to-meet-target/

function minimizeError(prices: string[], target: number): string {
    let floors = 0;
    const fracs: number[] = [];
    for (const p of prices) {
        const value = Number(p);
        const floor = Math.floor(value);
        floors += floor;
        const frac = value - floor;
        if (frac > 1e-9) fracs.push(frac);
    }
    const ceilCount = target - floors;
    if (ceilCount < 0 || ceilCount > fracs.length) return "-1";
    fracs.sort((a, b) => b - a);
    let error = 0;
    for (let i = 0; i < fracs.length; i++) {
        error += i < ceilCount ? 1 - fracs[i] : fracs[i];
    }
    return error.toFixed(3);
}
