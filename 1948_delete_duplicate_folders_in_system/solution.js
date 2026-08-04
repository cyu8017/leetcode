// LeetCode 1948 - Delete Duplicate Folders in System
// https://leetcode.com/problems/delete-duplicate-folders-in-system/

/**
 * @param {string[][]} paths
 * @return {string[][]}
 */
var deleteDuplicateFolder = function(paths) {
    const root = new Map();
    for (const path of paths) {
        let node = root;
        for (const folder of path) {
            if (!node.has(folder)) node.set(folder, new Map());
            node = node.get(folder);
        }
    }
    const dup = new Map();
    const serialOf = new WeakMap();
    const serialize = (node) => {
        if (!node.size) return "";
        const parts = [];
        for (const name of [...node.keys()].sort()) {
            parts.push(name + "(" + serialize(node.get(name)) + ")");
        }
        const serial = parts.join("");
        if (serial) {
            dup.set(serial, dup.has(serial));
            serialOf.set(node, serial);
        }
        return serial;
    };
    serialize(root);
    const ans = [];
    const collect = (node, path) => {
        for (const [name, child] of node) {
            const serial = serialOf.get(child) || "";
            if (serial && dup.get(serial)) continue;
            path.push(name);
            ans.push(path.slice());
            collect(child, path);
            path.pop();
        }
    };
    collect(root, []);
    return ans;
};
