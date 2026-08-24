# LeetCode 2306 - Naming a Company
# https://leetcode.com/problems/naming-a-company/

# @param {String[]} ideas
# @return {Integer}
def distinct_names(ideas)
  groups = Array.new(26) { {} }
  ideas.each do |idea|
    groups[idea[0].ord - 97][idea[1..]] = true
  end
  ans = 0
  (0...26).each do |i|
    ((i + 1)...26).each do |j|
      overlap = 0
      groups[i].each_key { |s| overlap += 1 if groups[j].key?(s) }
      ans += (groups[i].length - overlap) * (groups[j].length - overlap) * 2
    end
  end
  ans
end
