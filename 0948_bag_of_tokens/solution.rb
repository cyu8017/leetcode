# LeetCode 0948 - Bag of Tokens
# https://leetcode.com/problems/bag-of-tokens/

# @param {Integer[]} tokens
# @param {Integer} power
# @return {Integer}
def bag_of_tokens_score(tokens, power)
  tokens.sort!
  i = 0
  j = tokens.length - 1
  score = 0
  ans = 0
  while i <= j
    if power >= tokens[i]
      power -= tokens[i]
      i += 1
      score += 1
      ans = score if score > ans
    elsif score > 0
      power += tokens[j]
      j -= 1
      score -= 1
    else
      break
    end
  end
  ans
end
