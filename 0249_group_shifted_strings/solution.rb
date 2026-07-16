# LeetCode 0249 - Group Shifted Strings
# https://leetcode.com/problems/group-shifted-strings/

# @param {String[]} strings
# @return {String[][]}
def group_strings(strings)
  groups = {}
  strings.each do |text|
    key =
      if text.empty?
        ""
      else
        base = text.ord
        text.chars.map { |char| (char.ord - base) % 26 }.join(",")
      end
    groups[key] ||= []
    groups[key] << text
  end
  groups.values
end
