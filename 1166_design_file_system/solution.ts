// LeetCode 1166 - Design File System
// https://leetcode.com/problems/design-file-system/

class FileSystem {
    paths: any;

    constructor() {
        this.paths = new Map([["", -1]]);
    }

    createPath(path: string, value: number): boolean {
        if (this.paths.has(path)) return false;
        const parent = path.slice(0, path.lastIndexOf("/"));
        if (!this.paths.has(parent)) return false;
        this.paths.set(path, value);
        return true;
    }

    get(path: string): number {
        return this.paths.has(path) ? this.paths.get(path) : -1;
    }
}
