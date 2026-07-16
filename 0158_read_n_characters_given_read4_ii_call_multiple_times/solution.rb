# LeetCode 0158 - Read N Characters Given read4 II - Call Multiple Times
# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/

class Solution
  def read(file, queries)
    file_index = 0
    buffer = []
    results = []

    queries.each do |query|
      copied = 0
      while copied < query
        if buffer.empty?
          buffer = file[file_index, 4].to_s.chars
          file_index += buffer.length
          break if buffer.empty?
        end
        amount = [query - copied, buffer.length].min
        buffer.shift(amount)
        copied += amount
      end
      results << copied
    end
    results
  end
end