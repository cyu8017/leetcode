# LeetCode 0842 - Split Array into Fibonacci Sequence
# https://leetcode.com/problems/split-array-into-fibonacci-sequence/

# @param {String} num
# @return {Integer[]}
def split_into_fibonacci(num)
  n = num.length
  path = []

  dfs = lambda do |start|
    return path.length >= 3 if start == n

    (start...n).each do |finish|
      break if num[start] == "0" && finish > start

      val = num[start..finish].to_i
      break if val > 2**31 - 1

      if path.length >= 2
        total = path[-1] + path[-2]
        next if val < total
        break if val > total
      end
      path << val
      return true if dfs.call(finish + 1)

      path.pop
    end
    false
  end

  dfs.call(0)
  path
end
