# LeetCode 1307 - Verbal Arithmetic Puzzle\n# https://leetcode.com/problems/verbal-arithmetic-puzzle/\n\ndef is_solvable(words, result)
  return false if words.map(&:length).max > result.length
  return false if (words.join + result).chars.uniq.length > 10
  leading = {}
  (words + [result]).each { |word| leading[word[0]] = true if word.length > 1 }
  value = {}
  used = Array.new(10, false)
  width = result.length

  solve = lambda do |column, row, total|
    return total == 0 if column == width
    if row < words.length
      return solve.call(column, row + 1, total) if column >= words[row].length
      ch = words[row][-1 - column]
      return solve.call(column, row + 1, total + value[ch]) if value.key?(ch)
      (0...10).each do |digit|
        next if used[digit] || (digit == 0 && leading[ch])
        value[ch] = digit
        used[digit] = true
        return true if solve.call(column, row + 1, total + digit)
        used[digit] = false
        value.delete(ch)
      end
      return false
    end
    ch = result[-1 - column]
    digit = total % 10
    carry = total / 10
    if value.key?(ch)
      return value[ch] == digit && solve.call(column + 1, 0, carry)
    end
    return false if used[digit] || (digit == 0 && leading[ch])
    value[ch] = digit
    used[digit] = true
    ok = solve.call(column + 1, 0, carry)
    used[digit] = false
    value.delete(ch)
    ok
  end
  solve.call(0, 0, 0)
end
