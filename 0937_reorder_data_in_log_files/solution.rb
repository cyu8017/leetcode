# LeetCode 0937 - Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/

# @param {String[]} logs
# @return {String[]}
def reorder_log_files(logs)
  logs.sort_by.with_index do |log, idx|
    ident, rest = log.split(" ", 2)
    if rest[0] =~ /[A-Za-z]/
      [0, rest, ident, idx]
    else
      [1, idx]
    end
  end
end
