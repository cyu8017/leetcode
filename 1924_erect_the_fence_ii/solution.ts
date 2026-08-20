// LeetCode 1924 - Erect the Fence II
// https://leetcode.com/problems/erect-the-fence-ii/

function outerTrees(trees: number[][]): number[] {
    const pts: number[][] = trees.map((p) => [p[0], p[1]]);
    for (let i = pts.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [pts[i], pts[j]] = [pts[j], pts[i]];
    }
    const dist = (a: number[], b: number[]): number => Math.hypot(a[0] - b[0], a[1] - b[1]);
    const circle2 = (a: number[], b: number[]): [number[], number] => {
        const c = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2];
        return [c, dist(a, b) / 2];
    };
    const circle3 = (a: number[], b: number[], c: number[]): [number[], number] => {
        const [ax, ay] = a, [bx, by] = b, [cx, cy] = c;
        const d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by));
        if (Math.abs(d) < 1e-12) {
            const candidates = [circle2(a, b), circle2(a, c), circle2(b, c)];
            return candidates.reduce((best, cur) => (cur[1] < best[1] ? cur : best));
        }
        const ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d;
        const uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d;
        const center = [ux, uy];
        return [center, dist(center, a)];
    };
    const inside = (cir: [number[], number] | null, p: number[]): boolean =>
        !!cir && dist(cir[0], p) <= cir[1] + 1e-9;
    let circle: [number[], number] | null = null;
    for (let i = 0; i < pts.length; i++) {
        const p = pts[i];
        if (!circle || !inside(circle, p)) {
            circle = [p, 0.0];
            for (let j = 0; j < i; j++) {
                const q = pts[j];
                if (!inside(circle, q)) {
                    circle = circle2(p, q);
                    for (let k = 0; k < j; k++) {
                        const r = pts[k];
                        if (!inside(circle, r)) circle = circle3(p, q, r);
                    }
                }
            }
        }
    }
    return [circle![0][0], circle![0][1], circle![1]];
}
