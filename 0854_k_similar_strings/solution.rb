# LeetCode 0854 - K-Similar Strings
# https://leetcode.com/problems/k-similar-strings/

# @param {String} s1
# @param {String} s2
# @return {Integer}
def k_similarity(s1, s2)
  return 0 if s1 == s2

  target = s2
  queue = [[s1, 0]]
  seen = { s1 => true }

  neighbors = lambda do |s|
    arr = s.chars
    i = 0
    i += 1 while arr[i] == target[i]
    res = []
    ((i + 1)...arr.length).each do |j|
      next unless arr[j] == target[i] && arr[j] != target[j]

      arr[i], arr[j] = arr[j], arr[i]
      res << arr.join
      arr[i], arr[j] = arr[j], arr[i]
    end
    res
  end

  until queue.empty?
    cur, dist = queue.shift
    neighbors.call(cur).each do |nxt|
      return dist + 1 if nxt == target
      next if seen[nxt]

      seen[nxt] = true
      queue << [nxt, dist + 1]
    end
  end
  -1
end
