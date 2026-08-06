# LeetCode 1415 - The K Th Lexicographical String Of All Happy Strings Of Length N
# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

def get_happy_string(n, k)
  answer = []
  build = lambda do |path|
    if path.length == n
      answer << path
      return
    end
    'abc'.each_char do |char|
      build.call(path + char) if path.empty? || path[-1] != char
    end
  end
  build.call('')
  k <= answer.length ? answer[k - 1] : ''
end
