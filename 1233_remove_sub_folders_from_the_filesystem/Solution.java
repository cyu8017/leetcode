// LeetCode 1233 - Remove Sub-Folders from the Filesystem
// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

import java.util.*;

class Solution {
    public List<String> removeSubfolders(String[] folder) {
        Arrays.sort(folder);
        List<String> answer = new ArrayList<>();
        for (String path : folder) {
            if (answer.isEmpty() || !path.startsWith(answer.get(answer.size() - 1) + "/")) {
                answer.add(path);
            }
        }
        return answer;
    }
}

