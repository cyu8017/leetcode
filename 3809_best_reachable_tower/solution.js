// LeetCode 3809 - Best Reachable Tower
// https://leetcode.com/problems/best-reachable-tower/

var bestTower = function(towers, center, radius) {
    const cx = center[0], cy = center[1];
    let idx = -1;
    for (let i = 0; i < towers.length; i++) {
        const x = towers[i][0], y = towers[i][1], q = towers[i][2];
        const dist = Math.abs(x - cx) + Math.abs(y - cy);
        if (dist > radius) continue;
        if (idx === -1 || towers[idx][2] < q ||
            (towers[idx][2] === q &&
             (x < towers[idx][0] || (x === towers[idx][0] && y < towers[idx][1])))) {
            idx = i;
        }
    }
    if (idx === -1) return [-1, -1];
    return [towers[idx][0], towers[idx][1]];
};
