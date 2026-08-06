# LeetCode 1233 - Remove Sub-Folders from the Filesystem
# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

# @param {String[]} folder
# @return {String[]}
def remove_subfolders(folder)
  answer = []
  folder.sort.each do |path|
    answer << path if answer.empty? || !path.start_with?(answer[-1] + "/")
  end
  answer
end
