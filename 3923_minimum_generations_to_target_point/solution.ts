// LeetCode 3923 - Minimum Generations to Target Point
// https://leetcode.com/problems/minimum-generations-to-target-point/

export class P {
    constructor(a: any, b: any, c: any) {
    this.a = a; this.b = b; this.c = c;
}
    key(): any {
    return this.a + ',' + this.b + ',' + this.c;
}
}

export function minGenerations(points: any, target: any): any {
    const targetKey = target[0] + ',' + target[1] + ',' + target[2];
    const generation = new Map();
    const all = [];
    for (const values of points) {
        const p = new P(values[0], values[1], values[2]);
        generation.set(p.key(), 0);
        all.push(p);
    }
    if (generation.has(targetKey)) return generation.get(targetKey);
    for (let current = 1; ; current++) {
        const limit = all.length;
        const added = [];
        for (let i = 0; i < limit; i++) {
            for (let j = i + 1; j < limit; j++) {
                const pi = all[i], pj = all[j];
                if (pi.a === pj.a && pi.b === pj.b && pi.c === pj.c) continue;
                const p = new P(Math.floor((pi.a + pj.a) / 2), Math.floor((pi.b + pj.b) / 2), Math.floor((pi.c + pj.c) / 2));
                const key = p.key();
                if (!generation.has(key)) {
                    generation.set(key, current);
                    added.push(p);
                }
            }
        }
        if (generation.has(targetKey)) return generation.get(targetKey);
        if (added.length === 0) return -1;
        for (const p of added) all.push(p);
    }
}
