// LeetCode 0588 - Design In-Memory File System
// https://leetcode.com/problems/design-in-memory-file-system/

var FileSystem = function() {
    this.root = { isFile: false, content: "", children: new Map() };
};

/**
 * @param {string} path
 * @return {string[]}
 */
FileSystem.prototype.ls = function(path) {
    const split = (p) => p.split("/").filter(Boolean);
    if (path === "/") {
        return [...this.root.children.keys()].sort();
    }
    const parts = split(path);
    let node = this.root;
    for (const part of parts) node = node.children.get(part);
    if (node.isFile) return [parts[parts.length - 1]];
    return [...node.children.keys()].sort();
};

/**
 * @param {string} path
 * @return {void}
 */
FileSystem.prototype.mkdir = function(path) {
    let node = this.root;
    for (const part of path.split("/").filter(Boolean)) {
        if (!node.children.has(part)) node.children.set(part, { isFile: false, content: "", children: new Map() });
        node = node.children.get(part);
    }
};

/**
 * @param {string} filePath
 * @param {string} content
 * @return {void}
 */
FileSystem.prototype.addContentToFile = function(filePath, content) {
    const parts = filePath.split("/").filter(Boolean);
    let node = this.root;
    for (let i = 0; i + 1 < parts.length; ++i) {
        if (!node.children.has(parts[i])) node.children.set(parts[i], { isFile: false, content: "", children: new Map() });
        node = node.children.get(parts[i]);
    }
    const name = parts[parts.length - 1];
    if (!node.children.has(name)) node.children.set(name, { isFile: false, content: "", children: new Map() });
    const file = node.children.get(name);
    file.isFile = true;
    file.content += content;
};

/**
 * @param {string} filePath
 * @return {string}
 */
FileSystem.prototype.readContentFromFile = function(filePath) {
    let node = this.root;
    for (const part of filePath.split("/").filter(Boolean)) node = node.children.get(part);
    return node.content;
};
