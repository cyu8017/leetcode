# LeetCode 0756 - Pyramid Transition Matrix
# https://leetcode.com/problems/pyramid-transition-matrix/

# @param {String} bottom
# @param {String[]} allowed
# @return {Boolean}
def pyramid_transition(bottom, allowed)
  transitions = Hash.new { |h, k| h[k] = [] }
  allowed.each { |triple| transitions[triple[0, 2]] << triple[2] }
  memo = {}

  dfs = lambda do |row|
    return memo[row] if memo.key?(row)
    return memo[row] = true if row.length == 1

    options = []
    (0...(row.length - 1)).each do |i|
      choices = transitions[row[i, 2]]
      unless choices && !choices.empty?
        memo[row] = false
        return false
      end
      options << choices
    end

    build = lambda do |index, path|
      return dfs.call(path.join) if index == options.length

      options[index].each do |ch|
        path << ch
        return true if build.call(index + 1, path)

        path.pop
      end
      false
    end

    memo[row] = build.call(0, [])
  end

  dfs.call(bottom)
end
