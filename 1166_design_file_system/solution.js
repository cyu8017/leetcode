// LeetCode 1166 - Design File System
// https://leetcode.com/problems/design-file-system/

var FileSystem = function() {
    this.paths = new Map([["", -1]]);
};

/** 
 * @param {string} path 
 * @param {number} value
 * @return {boolean}
 */
FileSystem.prototype.createPath = function(path, value) {
    if (this.paths.has(path)) return false;
    const parent = path.slice(0, path.lastIndexOf("/"));
    if (!this.paths.has(parent)) return false;
    this.paths.set(path, value);
    return true;
};

/** 
 * @param {string} path
 * @return {number}
 */
FileSystem.prototype.get = function(path) {
    return this.paths.has(path) ? this.paths.get(path) : -1;
};
