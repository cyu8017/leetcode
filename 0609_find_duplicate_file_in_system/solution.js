// LeetCode 0609 - Find Duplicate File in System
// https://leetcode.com/problems/find-duplicate-file-in-system/

/**
 * @param {string[]} paths
 * @return {string[][]}
 */
var findDuplicate = function(paths) {
    const contentToPaths = new Map();
    for (const entry of paths) {
        const tokens = entry.split(" ");
        const directory = tokens[0];
        for (let i = 1; i < tokens.length; ++i) {
            const fileInfo = tokens[i];
            const open = fileInfo.indexOf("(");
            const name = fileInfo.substring(0, open);
            const content = fileInfo.substring(open + 1, fileInfo.length - 1);
            if (!contentToPaths.has(content)) contentToPaths.set(content, []);
            contentToPaths.get(content).push(directory + "/" + name);
        }
    }
    const result = [];
    for (const group of contentToPaths.values()) {
        if (group.length > 1) result.push(group);
    }
    return result;
};
