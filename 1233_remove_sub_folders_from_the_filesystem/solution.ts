// LeetCode 1233 - Remove Sub-Folders From The Filesystem
// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

function removeSubfolders(folder: string[]): string[] {
    const answer = [];
    for (const path of [...folder].sort()) {
        if (!answer.length || !path.startsWith(answer[answer.length - 1] + "/")) {
            answer.push(path);
        }
    }
    return answer;
}
