# LeetCode 3816 - Lexicographically Smallest String After Deleting Duplicate Characters
# https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/

# @param {String} s
# @return {String}
def lex_smallest_after_deletion(s)
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  stk = []
  s.each_char do |c|
    while !stk.empty? && stk[-1] > c && cnt[stk[-1].ord - 97] > 1
      cnt[stk[-1].ord - 97] -= 1
      stk.pop
    end
    stk << c
  end
  while cnt[stk[-1].ord - 97] > 1
    cnt[stk[-1].ord - 97] -= 1
    stk.pop
  end
  stk.join
end
