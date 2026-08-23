// LeetCode 3609 - Minimum Moves to Reach Target in Grid
// https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/

var minMoves = function(sx, sy, tx, ty) {
    let ans = 0;
    while (tx > sx || ty > sy) {
        if (tx < sx || ty < sy) return -1;
        if (tx === ty) return -1;
        if (tx > ty) {
            if (ty > sy) {
                if (tx >= 2 * ty) {
                    if (tx % 2 !== 0) return -1;
                    tx = Math.floor(tx / 2);
                } else {
                    tx -= ty;
                }
                ans++;
            } else {
                if (ty !== sy) return -1;
                while (tx > sx) {
                    if (tx >= 2 * ty) {
                        if (tx % 2 !== 0) return -1;
                        tx = Math.floor(tx / 2);
                    } else {
                        tx -= ty;
                    }
                    ans++;
                    if (tx < sx) return -1;
                }
            }
        } else {
            if (tx > sx) {
                if (ty >= 2 * tx) {
                    if (ty % 2 !== 0) return -1;
                    ty = Math.floor(ty / 2);
                } else {
                    ty -= tx;
                }
                ans++;
            } else {
                if (tx !== sx) return -1;
                while (ty > sy) {
                    if (ty >= 2 * tx) {
                        if (ty % 2 !== 0) return -1;
                        ty = Math.floor(ty / 2);
                    } else {
                        ty -= tx;
                    }
                    ans++;
                    if (ty < sy) return -1;
                }
            }
        }
    }
    return (tx === sx && ty === sy) ? ans : -1;
};
