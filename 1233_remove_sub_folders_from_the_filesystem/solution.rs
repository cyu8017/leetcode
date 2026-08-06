// LeetCode 1233 - Remove Sub-Folders from the Filesystem
// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

impl Solution {
    pub fn remove_subfolders(mut folder: Vec<String>) -> Vec<String> {
        folder.sort();
        let mut ans = Vec::new();
        for path in folder {
            if ans.is_empty() || !path.starts_with(&(ans.last().unwrap().clone() + "/")) {
                ans.push(path);
            }
        }
        ans
    }
}
