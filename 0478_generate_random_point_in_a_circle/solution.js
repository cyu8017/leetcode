// LeetCode 0478 - Generate Random Point in a Circle
// https://leetcode.com/problems/generate-random-point-in-a-circle/

let uniform = (a, b) => a + Math.random() * (b - a);

function set_uniform(uniformFn) {
    uniform = uniformFn;
}

class Solution {
    constructor(radius, xCenter, yCenter) {
        this.radius = radius;
        this.xCenter = xCenter;
        this.yCenter = yCenter;
    }

    randPoint() {
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

module.exports = { Solution, set_uniform, uniform };
