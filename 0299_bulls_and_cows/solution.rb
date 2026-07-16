# LeetCode 0299 - Bulls and Cows
# https://leetcode.com/problems/bulls-and-cows/

class Solution
  def getHint(secret, guess)
    bulls = 0
    secret_counts = {}
    guess_counts = {}
    secret.chars.zip(guess.chars).each do |secret_digit, guess_digit|
      if secret_digit == guess_digit
        bulls += 1
      else
        secret_counts[secret_digit] = secret_counts.fetch(secret_digit, 0) + 1
        guess_counts[guess_digit] = guess_counts.fetch(guess_digit, 0) + 1
      end
    end
    cows = guess_counts.sum { |digit, count| [count, secret_counts.fetch(digit, 0)].min }
    "#{bulls}A#{cows}B"
  end
end
