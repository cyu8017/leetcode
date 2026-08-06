# LeetCode 1598 - Crawler Log Folder
# https://leetcode.com/problems/crawler-log-folder/

# @param {String[]} logs
# @return {Integer}
def min_operations(logs)
  depth = 0
  logs.each do |log|
    if log == '../'
      depth = [0, depth - 1].max
    elsif log != './'
      depth += 1
    end
  end
  depth
end
