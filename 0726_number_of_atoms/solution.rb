# LeetCode 0726 - Number of Atoms
# https://leetcode.com/problems/number-of-atoms/

# @param {String} formula
# @return {String}
def count_of_atoms(formula)
  stack = [Hash.new(0)]
  i = 0
  n = formula.length

  while i < n
    if formula[i] == "("
      stack << Hash.new(0)
      i += 1
    elsif formula[i] == ")"
      i += 1
      start = i
      i += 1 while i < n && formula[i] >= "0" && formula[i] <= "9"
      mult = (formula[start...i].empty? ? "1" : formula[start...i]).to_i
      top = stack.pop
      top.each { |atom, count| stack[-1][atom] += count * mult }
    else
      start = i
      i += 1
      i += 1 while i < n && formula[i] >= "a" && formula[i] <= "z"
      atom = formula[start...i]
      start = i
      i += 1 while i < n && formula[i] >= "0" && formula[i] <= "9"
      count = (formula[start...i].empty? ? "1" : formula[start...i]).to_i
      stack[-1][atom] += count
    end
  end

  counts = stack.pop
  parts = []
  counts.keys.sort.each do |atom|
    parts << atom
    parts << counts[atom].to_s if counts[atom] > 1
  end
  parts.join
end
