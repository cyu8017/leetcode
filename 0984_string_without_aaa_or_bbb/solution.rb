# LeetCode 0984 - String Without AAA or BBB
# https://leetcode.com/problems/string-without-aaa-or-bbb/

# @param {Integer} a
# @param {Integer} b
# @return {String}
def str_without3a3b(a, b)
  ans = []
  while a > 0 || b > 0
    write_a = if ans.length >= 2 && ans[-1] == ans[-2]
                ans[-1] == "b"
              elsif ans.empty? && a.positive? && a <= b
                true
              else
                a > b
              end
    if write_a
      ans << "a"
      a -= 1
    else
      ans << "b"
      b -= 1
    end
  end
  ans.join
end
