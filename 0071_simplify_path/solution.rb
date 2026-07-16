# LeetCode 0071 - Simplify Path
# https://leetcode.com/problems/simplify-path/

# @param {String} path
# @return {String}
def simplify_path(path)
  stack = []

  path.split("/").each do |part|
    next if part.empty? || part == "."

    if part == ".."
      stack.pop unless stack.empty?
    else
      stack << part
    end
  end

  "/" + stack.join("/")
end
