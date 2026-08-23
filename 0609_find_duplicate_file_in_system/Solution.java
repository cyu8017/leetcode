// LeetCode 0609 - Find Duplicate File in System
// https://leetcode.com/problems/find-duplicate-file-in-system/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<List<String>> findDuplicate(String[] paths) {
        Map<String, List<String>> contentToPaths = new HashMap<>();
        for (String entry : paths) {
            String[] tokens = entry.split(" ");
            String directory = tokens[0];
            for (int i = 1; i < tokens.length; ++i) {
                String fileInfo = tokens[i];
                int open = fileInfo.indexOf('(');
                String name = fileInfo.substring(0, open);
                String content = fileInfo.substring(open + 1, fileInfo.length() - 1);
                contentToPaths.computeIfAbsent(content, k -> new ArrayList<>()).add(directory + "/" + name);
            }
        }
        List<List<String>> result = new ArrayList<>();
        for (List<String> group : contentToPaths.values()) {
            if (group.size() > 1) {
                result.add(group);
            }
        }
        return result;
    }
}
