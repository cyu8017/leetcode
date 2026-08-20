// LeetCode 1948 - Delete Duplicate Folders in System
// https://leetcode.com/problems/delete-duplicate-folders-in-system/

function deleteDuplicateFolder(paths: string[][]): string[][] {
    const root = new Map<string, any>();
    for (const path of paths) {
        let node = root;
        for (const folder of path) {
            if (!node.has(folder)) node.set(folder, new Map());
            node = node.get(folder);
        }
    }
    const dup = new Map<string, boolean>();
    const serialOf = new WeakMap<object, string>();
    const serialize = (node: Map<string, any>): string => {
        if (!node.size) return "";
        const parts: string[] = [];
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
    const ans: string[][] = [];
    const collect = (node: Map<string, any>, path: string[]): void => {
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
}
