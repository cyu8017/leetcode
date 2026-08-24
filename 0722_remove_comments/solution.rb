# LeetCode 0722 - Remove Comments
# https://leetcode.com/problems/remove-comments/

# @param {String[]} source
# @return {String[]}
def remove_comments(source)
  result = []
  buffer = []
  in_block = false

  source.each do |line|
    i = 0
    while i < line.length
      if in_block
        if i + 1 < line.length && line[i, 2] == "*/"
          in_block = false
          i += 2
        else
          i += 1
        end
      elsif i + 1 < line.length && line[i, 2] == "/*"
        in_block = true
        i += 2
      elsif i + 1 < line.length && line[i, 2] == "//"
        break
      else
        buffer << line[i]
        i += 1
      end
    end

    if !in_block && !buffer.empty?
      result << buffer.join
      buffer = []
    end
  end

  result
end
