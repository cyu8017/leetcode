// LeetCode 1274 - Number of Ships in a Rectangle
// https://leetcode.com/problems/number-of-ships-in-a-rectangle/

interface Sea {
    hasShips(topRight: number[], bottomLeft: number[]): boolean;
}

function countShips(sea: Sea, topRight: number[], bottomLeft: number[]): number {
    const tx = topRight[0];
    const ty = topRight[1];
    const bx = bottomLeft[0];
    const by = bottomLeft[1];
    if (tx < bx || ty < by || !sea.hasShips(topRight, bottomLeft)) return 0;
    if (tx === bx && ty === by) return 1;
    const mx = Math.floor((tx + bx) / 2);
    const my = Math.floor((ty + by) / 2);
    return (
        countShips(sea, [mx, my], bottomLeft)
        + countShips(sea, [tx, my], [mx + 1, by])
        + countShips(sea, [mx, ty], [bx, my + 1])
        + countShips(sea, topRight, [mx + 1, my + 1])
    );
}
