// LeetCode 2069 - Walking Robot Simulation II
// https://leetcode.com/problems/walking-robot-simulation-ii/

export class Robot {
    constructor(width: any, height: any) {
        this.w = width;
        this.h = height;
        this.peri = 2 * (width + height) - 4;
        this.pos = 0;
        this.moved = false;
    }

    getPosDir(): any {
        let p = this.pos;
        if (p === 0) {
            if (!this.moved) return [0, 0, 0];
            return [0, 0, 3];
        }
        if (p <= this.w - 1) return [p, 0, 0];
        p -= this.w - 1;
        if (p <= this.h - 1) return [this.w - 1, p, 1];
        p -= this.h - 1;
        if (p <= this.w - 1) return [this.w - 1 - p, this.h - 1, 2];
        p -= this.w - 1;
        return [0, this.h - 1 - p, 3];
    }

    step(num: any): any {
        this.moved = true;
        this.pos = (this.pos + num) % this.peri;
    }

    getPos(): any {
        const pd = this.getPosDir();
        return [pd[0], pd[1]];
    }

    getDir(): any {
        const names = ["East", "North", "West", "South"];
        return names[this.getPosDir()[2]];
    }
}
