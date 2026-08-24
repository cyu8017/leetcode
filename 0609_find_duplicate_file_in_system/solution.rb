# LeetCode 0609 - Find Duplicate File in System
# https://leetcode.com/problems/find-duplicate-file-in-system/

# @param {String[]} paths
# @return {String[][]}
def find_duplicate(paths)
  content_to_paths = Hash.new { |h, k| h[k] = [] }

  paths.each do |entry|
    parts = entry.split(" ")
    directory = parts[0]
    parts[1..].each do |file_info|
      name, rest = file_info.split("(", 2)
      content = rest[0...-1]
      content_to_paths[content] << "#{directory}/#{name}"
    end
  end

  content_to_paths.values.select { |group| group.length > 1 }.reverse
end
