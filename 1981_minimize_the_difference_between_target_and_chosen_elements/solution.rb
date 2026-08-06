# LeetCode 1981 - Minimize the Difference Between Target and Chosen Elements
# https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/

# @param {Integer[][]} mat
# @param {Integer} target
# @return {Integer}
def minimize_the_difference(mat, target)
  possible = { 0 => true }
  mat.each do |row|
    nxt = {}
    possible.each_key do |s|
      row.uniq.each { |x| nxt[s + x] = true }
    end
    kept = {}
    above = []
    nxt.each_key do |v|
      if v <= target
        kept[v] = true
      else
        above << v
      end
    end
    kept[above.min] = true unless above.empty?
    possible = kept.empty? ? { nxt.keys.min => true } : kept
  end
  possible.keys.map { |v| (v - target).abs }.min
end
