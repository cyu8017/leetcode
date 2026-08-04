// LeetCode 1233 - Remove Sub-Folders From The Filesystem
// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

/**
 * @param {string[]} folder
 * @return {string[]}
 */
var removeSubfolders = function(folder) {
    const answer = [];
    for (const path of [...folder].sort()) {
        if (!answer.length || !path.startsWith(answer[answer.length - 1] + "/")) {
            answer.push(path);
        }
    }
    return answer;
};
