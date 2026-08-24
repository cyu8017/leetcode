# LeetCode 2227 - Encrypt and Decrypt Strings
# https://leetcode.com/problems/encrypt-and-decrypt-strings/

class Encrypter
  def initialize(keys, values, dictionary)
    @enc = {}
    @cnt = Hash.new(0)
    keys.each_with_index { |k, i| @enc[k] = values[i] }
    dictionary.each { |w| @cnt[encrypt(w)] += 1 }
  end

  def encrypt(word1)
    b = []
    word1.each_char do |c|
      return "" unless @enc.key?(c)

      b << @enc[c]
    end
    b.join
  end

  def decrypt(word2)
    @cnt[word2]
  end
end
