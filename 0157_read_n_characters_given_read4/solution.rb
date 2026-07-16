# LeetCode 0157 - Read N Characters Given Read4
# https://leetcode.com/problems/read-n-characters-given-read4/

class Solution
  def read(file, n)
    file_index = 0
    copied = 0
    while copied < n && file_index < file.length
      count = [4, file.length - file_index].min
      file_index += count
      copied += [count, n - copied].min
    end
    copied
  end
end