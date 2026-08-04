// LeetCode 1233 - Remove Sub-Folders from the Filesystem
// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution {
    fun removeSubfolders(folder: Array<String>): List<String> {
        folder.sort()
        val answer = mutableListOf<String>()
        for (path in folder) {
            if (answer.isEmpty() || !path.startsWith(answer.last() + "/")) answer.add(path)
        }
        return answer
    }
}
