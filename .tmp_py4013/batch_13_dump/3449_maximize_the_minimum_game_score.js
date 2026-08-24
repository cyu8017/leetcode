// LeetCode 3449 - Maximize the Minimum Game Score
// https://leetcode.com/problems/maximize-the-minimum-game-score/

var maxScore = function(points, m) {
    const ok = (mid) => {
        let need = 0n, extra = 0n;
        const mm = BigInt(m);
        for (const p of points) {
            const pp = BigInt(p);
            const req = (mid + pp - 1n) / pp;
            if (req > extra) {
                const visits = req - extra;
                need += 2n * visits - 1n;
                extra = visits - 1n;
            } else {
                need += 1n;
                extra = 0n;
            }
            if (need > mm) return false;
        }
        return need <= mm;
    };
    let lo = 0n, hi = 10n ** 18n;
    while (lo < hi) {
        const mid = (lo + hi + 1n) / 2n;
        if (ok(mid)) lo = mid;
        else hi = mid - 1n;
    }
    return Number(lo);
};
