// LeetCode 3391 - Design a 3D Binary Matrix with Efficient Layer Tracking
// https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/

export class Matrix3D {
    constructor(n: any) {
    this.n = n;
    this.m = Array.from({length: n}, () =>
        Array.from({length: n}, () => new Array(n).fill(0)));
    this.ones = new Array(n).fill(0);
}
    setCell(x: any, y: any, z: any): any {
    if (this.m[x][y][z] === 0) {
        this.m[x][y][z] = 1;
        this.ones[x]++;
    }
}
    unsetCell(x: any, y: any, z: any): any {
    if (this.m[x][y][z] === 1) {
        this.m[x][y][z] = 0;
        this.ones[x]--;
    }
}
    largestMatrix(): any {
    let best = -1, idx = 0;
    for (let i = 0; i < this.n; i++) {
        if (this.ones[i] >= best) {
            best = this.ones[i];
            idx = i;
        }
    }
    return idx;
}
}
