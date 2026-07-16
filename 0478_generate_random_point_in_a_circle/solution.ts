// LeetCode 0478 - Generate Random Point in a Circle
// https://leetcode.com/problems/generate-random-point-in-a-circle/

type UniformFn = (a: number, b: number) => number;

let uniform: UniformFn = (a, b) => a + Math.random() * (b - a);

export function set_uniform(uniformFn: UniformFn): void {
    uniform = uniformFn;
}

export class Solution {
    private radius: number;
    private xCenter: number;
    private yCenter: number;

    constructor(radius: number, xCenter: number, yCenter: number) {
        this.radius = radius;
        this.xCenter = xCenter;
        this.yCenter = yCenter;
    }

    randPoint(): number[] {
        while (true) {
            const x = uniform(-this.radius, this.radius);
            const y = uniform(-this.radius, this.radius);
            if (x * x + y * y <= this.radius * this.radius) {
                return [
                    Number((this.xCenter + x).toFixed(5)),
                    Number((this.yCenter + y).toFixed(5)),
                ];
            }
        }
    }
}

export { uniform };
