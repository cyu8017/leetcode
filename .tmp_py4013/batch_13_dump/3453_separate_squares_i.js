// LeetCode 3453 - Separate Squares I
// https://leetcode.com/problems/separate-squares-i/

var separateSquares = function(squares) {
    let total = 0;
    for (const sq of squares) {
        const l = sq[2];
        total += l * l;
    }
    const areaBelow = (y) => {
        let below = 0;
        for (const sq of squares) {
            const yi = sq[1], l = sq[2];
            const top = yi + l;
            if (y <= yi) continue;
            if (y >= top) below += l * l;
            else below += l * (y - yi);
        }
        return below;
    };
    let lo = 0.0, hi = 2e9;
    for (let it = 0; it < 60; it++) {
        const mid = (lo + hi) / 2;
        if (areaBelow(mid) * 2 < total) lo = mid;
        else hi = mid;
    }
    return hi;
};
