// LeetCode 3464 - Maximize the Distance Between Points on a Square
// https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

var maxDistance = function(side, points, k) {
    const canPlace = (arr, perim, mid) => {
        const n = arr.length;
        for (let s = 0; s < n; s++) {
            let cnt = 1;
            let last = arr[s];
            let idx = s;
            for (; cnt < k; ) {
                const target = last + mid;
                let found = false;
                for (let step = 1; step < n; step++) {
                    const ni = (idx + step) % n;
                    const val = arr[ni];
                    const add = ni <= idx ? perim : 0;
                    if (val + add >= target) {
                        last = val + add;
                        idx = ni;
                        cnt++;
                        found = true;
                        break;
                    }
                }
                if (!found) break;
            }
            if (cnt === k && last - arr[s] <= perim - mid) return true;
        }
        return false;
    };
    const arr = new Array(points.length);
    for (let i = 0; i < points.length; i++) {
        const x = points[i][0], y = points[i][1];
        let d;
        if (y === 0) d = x;
        else if (x === side) d = side + y;
        else if (y === side) d = 2 * side + (side - x);
        else d = 3 * side + (side - y);
        arr[i] = d;
    }
    arr.sort((a, b) => a - b);
    const perim = 4 * side;
    let lo = 0, hi = 2 * side;
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (canPlace(arr, perim, mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
};
