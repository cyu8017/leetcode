// LeetCode 2013 - Detect Squares
// https://leetcode.com/problems/detect-squares/

export class DetectSquares {
    constructor() {
        this.cnt = new Map();
    }

    key(x: any, y: any): any {
        return x + "," + y;
    }

    add(point: any): any {
        const k = this.key(point[0], point[1]);
        this.cnt.set(k, (this.cnt.get(k) || 0) + 1);
    }

    count(point: any): any {
        const x = point[0], y = point[1];
        let ans = 0;
        for (const [k, c] of this.cnt) {
            const [px, py] = k.split(",").map(Number);
            if (px === x || py === y) continue;
            if (Math.abs(px - x) !== Math.abs(py - y)) continue;
            const c1 = this.cnt.get(this.key(px, y)) || 0;
            const c2 = this.cnt.get(this.key(x, py)) || 0;
            ans += c * c1 * c2;
        }
        return ans;
    }
}
